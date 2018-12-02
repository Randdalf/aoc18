#!/usr/bin/env python

"""Advent of Code 2018, Day 2, Puzzle 1"""

from d2 import puzzle

def solve(ids):
    twos = 0
    threes = 0
    for id in ids:
        counts = [0 for i in range(26)]
        for c in id:
            counts[ord(c) - ord('a')] += 1
        twos += int(any(map(lambda x: x == 2, counts)))
        threes += int(any(map(lambda x: x == 3, counts)))
    return twos * threes

def main():
    print(solve(puzzle()))

if __name__ == "__main__":
    main()
