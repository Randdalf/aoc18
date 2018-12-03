#!/usr/bin/env python

"""Advent of Code 2018, Day 3, Puzzle 1"""

from collections import Counter

from d3 import puzzle

def squares(rects):
    for r in rects:
        for x in range(r.l, r.r):
            for y in range(r.t, r.b):
                yield (x, y)

def solve(rects):
    counter = Counter(squares(rects))
    return sum(map(lambda x: int(x >= 2), counter.values()))

def main():
    print(solve(puzzle()))

if __name__ == "__main__":
    main()
