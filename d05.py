#!/usr/bin/env python

"""Advent of Code 2018, Day 5"""

import threading

from aoc18 import solve

# Build a LUT for the reactions.
reactions = []
for i in range(128):
    c = chr(i)
    if c.isupper():
        reactions.append(c.lower())
    elif c.islower():
        reactions.append(c.upper())
    else:
        reactions.append(c)

def parse(data):
    return data

def react(polymer):
    stack = []
    for unit in polymer:
        if len(stack) > 0 and reactions[ord(unit)] == stack[-1]:
            stack.pop()
        else:
            stack.append(unit)
    return stack

def len_react(polymer):
    return len(react(polymer))

def improve(polymer):
    # React the polymer without a unit type removed. This reduces the amount of
    # work we have to when iterating over each unit type.
    polymer = react(polymer)
    return min(map(lambda c: len_react(filter(lambda x: x.lower() != c, polymer)), map(chr, range(ord('a'),ord('z')+1))))

if __name__ == "__main__":
    solve(5, parse, len_react, improve)
