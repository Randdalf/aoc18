#!/usr/bin/env python

"""Advent of Code 2018, Day 23"""

import re
from math import log
from math import ceil
from random import randint
from random import uniform

from aoc18 import solve

def parse(data):
    pattern = re.compile("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")
    return [tuple(map(int, re.match(pattern, x).groups())) for x in data.splitlines()]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def in_range(pos, bot):
    return dist(pos, bot) <= bot[3]

def in_range_of_largest_radius(bots):
    strongest = max(bots, key=lambda b: b[3])
    radius = strongest[3]
    return sum(int(in_range(bot, strongest)) for bot in bots)

def score(pos, bots):
    # 1: Maximise number of in-range bots.
    # 2: Minimise distance from origin.
    return (sum(int(in_range(pos, bot)) for bot in bots), -dist(pos, (0,0,0)))

def neighbors(pos, offsets):
    x0 = pos[0]
    y0 = pos[1]
    z0 = pos[2]
    for offset in offsets:
        for sign in [-1, +1]:
            s = sign * offset
            x1 = x0 + s
            y1 = y0 + s
            z1 = z0 + s
            yield(x0, y0, z1)
            yield(x0, y1, z0)
            yield(x0, y1, z1)
            yield(x1, y0, z0)
            yield(x1, y0, z1)
            yield(x1, y1, z0)
            yield(x1, y1, z1)

def in_range_of_most_nanobots(bots):
    # Calculate size of world to limit number of neighbors.
    gmin = [min(z) for z in zip(*[tuple(x - b[3] for x in b[:3]) for b in bots])]
    gmax = [max(z) for z in zip(*[tuple(x + b[3] for x in b[:3]) for b in bots])]
    size = max([x-n for n,x in zip(gmin, gmax)])
    max_k = ceil(log(size / 2, 2))
    offsets = [2**k for k in range(max_k+1)]

    # Hill climb the problem space.
    curr = (0,0,0)
    curr_score = score(curr, bots)
    improved = True

    while improved:
        improved = False
        for neighbor in neighbors(curr, offsets):
            n_score = score(neighbor, bots)
            if n_score > curr_score:
                curr = neighbor
                curr_score = n_score
                improved = True

    return -curr_score[1]

if __name__ == "__main__":
    solve(23, parse, in_range_of_largest_radius, in_range_of_most_nanobots)
