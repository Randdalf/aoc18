#!/usr/bin/env python

"""Advent of Code 2018, Day 1, Puzzle 1"""

from d1 import puzzle

def solve(deltas):
    return sum(deltas)

def main():
    print(solve(puzzle()))

if __name__ == "__main__":
    main()
