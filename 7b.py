#!/usr/bin/python3

import gates


def parse():
    with open("input/7", "r") as input:
        return gates.parse_gates(input)


logic_gates = parse()
a = logic_gates.get("a")

# reset
logic_gates = parse()
logic_gates.add_gate("b", a)
print(logic_gates.get("a"))
