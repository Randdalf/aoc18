#!/usr/bin/env python

"""Advent of Code 2018, Day 3, Puzzle 2"""

from collections import Counter

from d3 import puzzle
from d3p1 import squares

def solve(rects):
    rects = list(rects)
    counter = Counter(squares(rects))

    for r in rects:
        if all(map(lambda x: counter[x] == 1, r.squares())):
            return r.id


def main():
    print(solve(puzzle()))

if __name__ == "__main__":
    main()
