#!/usr/bin/env python

"""Advent of Code 2018, Day 1, Puzzle 2"""

from d1 import puzzle

def solve(deltas):
    deltas = list(deltas)
    frequency = 0
    seen = set()
    while True:
        for delta in deltas:
            seen.add(frequency)
            frequency += delta
            if frequency in seen:
                return frequency

def main():
    print(solve(puzzle()))

if __name__ == "__main__":
    main()
