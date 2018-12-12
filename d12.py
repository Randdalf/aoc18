#!/usr/bin/env python

"""Advent of Code 2018, Day 12"""

import re

from aoc18 import solve

def parse(data):
    state_pattern = re.compile("initial state: ([#.]+)")
    rule_pattern = re.compile("([#.]+) => ([#.])")
    lines = data.splitlines()
    state = re.match(state_pattern, lines[0]).group(1)
    rules = set(map(lambda x: x.group(1), filter(lambda x: x.group(2) == '#', map(lambda x: re.match(rule_pattern, x), lines[2:]))))
    return (state, rules)

def simulate(state, rules, offset, gens):
    for i in range(gens):
        state = '....' + state + '....'
        n = len(state)
        next = []
        for x in range(0, n-5):
            next.append('#' if state[x:x+5] in rules else '.')
        offset += next.index('#') - 2
        state = ''.join(next).strip('.')
    return (state, offset)

def sum_of_plants(state, offset):
    return sum(map(lambda i: i + offset, filter(lambda i: state[i] == '#', range(len(state)))))

def sum_after_20_gens(data):
    state, offset = simulate(data[0], data[1], 0, 20)
    return sum_of_plants(state, offset)

def sum_after_50000000000_gens(data):
    n = 50000000000
    state = data[0]
    rules = data[1]
    offset = 0
    seen = set([state])
    for g in range(n):
        state, offset = simulate(state, rules, offset, 1)
        if state in seen:
            return sum_of_plants(state, n - g - 1 + offset)
        seen.add(state)

if __name__ == "__main__":
    solve(12, parse, sum_after_20_gens, sum_after_50000000000_gens)
