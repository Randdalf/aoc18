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
        if r[2] == 29:
            return r[4]

if __name__ == "__main__":
    solve(21, parse, run_until_halt_opportunity)
