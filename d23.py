#!/usr/bin/env python

"""Advent of Code 2018, Day 23"""

import re

from aoc18 import solve

def parse(data):
    pattern = re.compile("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")
    return [tuple(map(int, re.match(pattern, x).groups())) for x in data.splitlines()]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def in_range_of_largest_radius(bots):
    strongest = max(bots, key=lambda b: b[3])
    radius = strongest[3]
    return sum(int(dist(bot, strongest) <= radius) for bot in bots)

if __name__ == "__main__":
    solve(23, parse, in_range_of_largest_radius)
