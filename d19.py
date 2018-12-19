#!/usr/bin/env python

"""Advent of Code 2018, Day 19"""

import math

from aoc18 import solve
from cpu import ops

class Program:
    def __init__(slf, ipr, instrs):
        slf.ipr = ipr
        slf.instrs = instrs

def parse(data):
    lines = data.splitlines()
    ipr = int(lines[0].split(' ')[1])
    ops_by_name = {op.__name__: op for op in ops}
    instrs = []
    for line in lines[1:]:
        parts = line.split(' ')
        instrs.append((ops_by_name[parts[0]], tuple(map(int, parts[1:]))))
    return Program(ipr, instrs)

def execute(program, r, max_cycles):
    ip = 0
    ipr = program.ipr
    instrs = program.instrs
    cycle = 0
    while 0 <= ip < len(instrs) and cycle < max_cycles:
        r[ipr] = ip
        instr = instrs[ip]
        instr[0](r, *instr[1])
        ip = r[ipr] + 1
        cycle += 1
    return r[0]

def sum_factors(program, r0):
    r = [r0,0,0,0,0,0]
    execute(program, r, 20)
    n = r[5]
    sqrt_n = math.sqrt(n)
    i = 1
    sum = 0
    while i <= sqrt_n:
        if n % i == 0:
            sum += i + n / i
        i += 1
    return int(sum)

if __name__ == "__main__":
    solve(19, parse, lambda p: sum_factors(p, 0), lambda p: sum_factors(p, 1))
