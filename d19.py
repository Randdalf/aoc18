#!/usr/bin/env python

"""Advent of Code 2018, Day 19"""

import math

from aoc18 import solve
from cpu import parse
from cpu import execute

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
