#!/usr/bin/env python

"""Advent of Code 2018, Day 22"""

import re

from aoc18 import solve

def parse(data):
    lines = data.splitlines()
    dp = re.compile('depth: (\d+)')
    tp = re.compile('target: (\d+),(\d+)')
    dm = re.match(dp, lines[0])
    tm = re.match(tp, lines[1])
    return (int(dm.group(1)), (int(tm.group(1)), int(tm.group(2))))

def risk_level(depth, target):
    erosion = []
    risk_level = 0
    w = target[0] + 1
    h = target[1] + 1
    for y in range(h):
        for x in range(w):
            if (x,y) == (0,0) or (x,y) == target:
                geologic_index = 0
            elif y == 0:
                geologic_index = x * 16807
            elif x == 0:
                geologic_index = y * 48271
            else:
                index = len(erosion)
                geologic_index = erosion[index-1] * erosion[index-w]
            erosion.append((geologic_index + depth) % 20183)
    return sum([e % 3 for e in erosion])

if __name__ == "__main__":
    solve(22, parse, lambda x: risk_level(*x))
