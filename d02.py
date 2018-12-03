#!/usr/bin/env python

"""Advent of Code 2018, Day 2"""

import itertools

from aoc18 import solve

def parse(data):
    return data.split('\n')

def checksum_ids(ids):
    twos = 0
    threes = 0
    for id in ids:
        counts = [0 for i in range(26)]
        for c in id:
            counts[ord(c) - ord('a')] += 1
        twos += int(any(map(lambda x: x == 2, counts)))
        threes += int(any(map(lambda x: x == 3, counts)))
    return twos * threes

def intersect_closest_ids(ids):
    for (id1,id2) in itertools.combinations(ids, 2):
        sum = 0
        mismatch = None
        for i, (a,b) in enumerate(zip(id1, id2)):
            if a != b:
                sum += 1
                mismatch = i
        if sum == 1:
            return id1[:mismatch] + id1[mismatch+1:]

if __name__ == "__main__":
    solve(2, parse, checksum_ids, intersect_closest_ids)
