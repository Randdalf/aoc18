#!/usr/bin/env python

"""Advent of Code 2018, Day 5"""

from aoc18 import solve

def parse(data):
    return data

def units_react(a, b):
    return a != b and a.lower() == b.lower()

def react(polymer):
    stack = []
    for unit in polymer:
        if len(stack) > 0 and units_react(unit, stack[-1]):
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)

if __name__ == "__main__":
    solve(5, parse, react)
