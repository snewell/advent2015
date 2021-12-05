#!/usr/bin/python3

import aoc
import gates


def _run(reader):
    logic_gates = gates.parse_gates(reader)
    return logic_gates.get("a")


aoc.load(_run)
