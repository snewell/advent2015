import re


def _value_or_ref(value, gates):
    if value.isdigit():
        return int(value)
    return gates.get(value)


def _make_value_circuit(value):
    return lambda gates: value


def _make_ref_circuit(ref):
    def execute(gates):
        result = gates.get(ref)
        return result

    return execute


def _make_not_circuit(operand):
    def execute(gates):
        result = ~_value_or_ref(operand, gates)
        result &= 0xFFFF
        return result

    return execute


def _make_and_circuit(lhs, rhs):
    def execute(gates):
        real_lhs = _value_or_ref(lhs, gates)
        real_rhs = _value_or_ref(rhs, gates)
        result = real_lhs & real_rhs
        return result

    return execute


def _make_or_circuit(lhs, rhs):
    def execute(gates):
        real_lhs = _value_or_ref(lhs, gates)
        real_rhs = _value_or_ref(rhs, gates)
        result = real_lhs | real_rhs
        return result

    return execute


def _make_lshift_circuit(lhs, amount):
    def execute(gates):
        real_lhs = _value_or_ref(lhs, gates)
        result = real_lhs << amount
        result &= 0xFFFF
        return result

    return execute


def _make_rshift_circuit(lhs, amount):
    def execute(gates):
        real_lhs = _value_or_ref(lhs, gates)
        result = real_lhs >> amount
        return result

    return execute


class Gates:
    def __init__(self):
        self._gates = {}

    def add_gate(self, name, logic_fn):
        self._gates[name] = logic_fn

    def get(self, name):
        result = self._gates[name]
        if isinstance(result, int):
            return result
        real_result = result(self)
        self._gates[name] = real_result
        return real_result


_RULE_RE = re.compile(R"^(.+) -> ([a-z]+)$")

_PARSE_HANDLERS = {
    "AND": lambda lhs, rhs: _make_and_circuit(lhs, rhs),
    "OR": lambda lhs, rhs: _make_or_circuit(lhs, rhs),
    "LSHIFT": lambda lhs, rhs: _make_lshift_circuit(lhs, int(rhs)),
    "RSHIFT": lambda lhs, rhs: _make_rshift_circuit(lhs, int(rhs)),
}


def _parse_single_gate(line):
    if line:
        match = _RULE_RE.match(line)
        if match:
            name = match.group(2)
            rule = match.group(1)

            rule_args = rule.split(" ")
            if len(rule_args) > 1:
                # actual logic gate
                if rule_args[0] == "NOT":
                    return _make_not_circuit(rule_args[1]), name
                else:
                    lhs = rule_args[0]
                    rhs = rule_args[2]
                    gate = _PARSE_HANDLERS[rule_args[1]](lhs, rhs)
                    return gate, name
            else:
                if rule.isdigit():
                    value = int(rule)
                    return _make_value_circuit(value), name
                else:
                    return _make_ref_circuit(rule), name
    # skip any blank lines
    return None, None


def parse_gates(reader):
    ret = Gates()
    line = reader.readline()
    while line:
        gate, name = _parse_single_gate(line)
        if gate:
            ret.add_gate(name, gate)
        line = reader.readline()
    return ret
