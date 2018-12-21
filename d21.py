#!/usr/bin/env python

"""Advent of Code 2018, Day 21"""

from math import inf

from aoc18 import solve
from cpu import parse
from cpu import execute

def run_until_halt_opportunity(program):
    ip = 0
    r = [0,0,0,0,0,0]
    while True:
        ip = execute(program, r, 1, ip)
        if ip == 28:
            instr = program.instrs[ip]
            return r[instr[1][0]]

def run_until_seen(program):
    r0 = 0
    r4 = 0
    seen = set()
    prev = None
    while True:
        r1 = r4 | 65536
        r4 = 16031208
        while True:
            r4 = (((r4 + (r1 & 255)) & 16777215) * 65899) & 16777215
            if 256 > r1:
                break
            r1 = r1 // 256
        if r4 in seen:
            return prev
        seen.add(r4)
        prev = r4

if __name__ == "__main__":
    solve(21, parse, run_until_halt_opportunity, run_until_seen)
