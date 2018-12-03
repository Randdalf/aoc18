#!/usr/bin/env python

"""Advent of Code 2018, Day 3, Puzzle 1"""

from collections import Counter

from d3 import puzzle

def squares(rects):
    for r in rects:
        yield from r.squares()

def solve(rects):
    counter = Counter(squares(rects))
    return sum(map(lambda x: int(x >= 2), counter.values()))

def main():
    print(solve(puzzle()))

if __name__ == "__main__":
    main()
