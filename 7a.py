#!/usr/bin/python3

import gates


def parse():
    with open("input/7", "r") as input:
        return gates.parse_gates(input)


logic_gates = parse()
print(logic_gates.get("a"))
# for name, gate in logic_gates._gates.items():
# print("{} -> {}".format(name, gate(logic_gates._gates)))
