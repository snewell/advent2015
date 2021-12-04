#!/usr/bin/python3

import gates


def parse():
    with open("input/7", "r") as input:
        return gates.parse_gates(input)


logic_gates = parse()
a = logic_gates.get("a")

# reset
logic_gates.clear_cache()
logic_gates.add_cache_entry("b", a)
print(logic_gates.get("a"))
