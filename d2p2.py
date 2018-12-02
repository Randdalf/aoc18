#!/usr/bin/env python

"""Advent of Code 2018, Day 2, Puzzle 2"""

import itertools

from d2 import puzzle

def solve(ids):
    for (id1,id2) in itertools.combinations(ids, 2):
        sum = 0
        mismatch = None
        for i, (a,b) in enumerate(zip(id1, id2)):
            if a != b:
                sum += 1
                mismatch = i
        if sum == 1:
            return id1[:mismatch] + id1[mismatch+1:]

def main():
    print(solve(puzzle()))

if __name__ == "__main__":
    main()
