#!/usr/bin/env python

"""Advent of Code 2018, Day 7"""

import re
import operator
import itertools
import collections

from aoc18 import solve

def parse(data):
    pattern = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
    return [re.match(pattern, line).groups() for line in data.splitlines()]

def determine_order(instructions):
    outputs = collections.defaultdict(list)
    for a,b in instructions:
        outputs[a].append(b)

    outstanding = collections.defaultdict(int)
    for b,a in map(reversed, instructions):
        outstanding[b] += 1

    steps = sorted(list(set(itertools.chain.from_iterable(instructions))))

    order = []
    while len(steps) > 0:
        step = next(x for x in steps if outstanding[x] == 0)
        steps.remove(step)
        order.append(step)
        for output in outputs[step]:
            outstanding[output] -= 1

    return ''.join(order)

if __name__ == "__main__":
    solve(7, parse, determine_order)
