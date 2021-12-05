#!/usr/bin/python3

import aoc
import gates


def _run(reader):
    logic_gates = gates.parse_gates(reader)
    a = logic_gates.get("a")
    # reset
    logic_gates.clear_cache()
    logic_gates.add_cache_entry("b", a)
    return logic_gates.get("a")


aoc.load(_run)
