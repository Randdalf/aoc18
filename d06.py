#!/usr/bin/env python

"""Advent of Code 2018, Day 6"""

import functools
import collections

from aoc18 import solve

class Coord:
    def __init__(slf, x, y):
        slf.x = x
        slf.y = y

    def __add__(slf, otr):
        return Coord(slf.x + otr.x, slf.y + otr.y)

    def __sub__(slf, otr):
        return Coord(slf.x - otr.x, slf.y - otr.y)

    def __str__(slf):
        return f'({slf.x}, {slf.y})'

def dist(a, b):
    return abs(b.x - a.x) + abs(b.y - a.y)

def coord_min(a, b):
    return Coord(min(a.x, b.x), min(a.y, b.y))

def coord_max(a, b):
    return Coord(max(a.x, b.x), max(a.y, b.y))

def parse(data):
    coords = []
    for line in data.splitlines():
        elems = line.split(',')
        coords.append(Coord(int(elems[0]), int(elems[1])))
    return coords

def row_major(x, y, w):
    return w * y + x

def largest_finite_area(coords):
    # Transform the coords relative to (0,0)
    umin = functools.reduce(coord_min, coords)
    umax = functools.reduce(coord_max, coords) + Coord(1,1)
    offset = Coord(1, 1)
    ncoords = []
    nmin = Coord(0, 0)
    nmax = umax - umin + offset
    for coord in coords:
        ncoords.append(coord - umin + offset)

    # Build a grid storing the closest ncoord index to each point. (or -1 if
    # there were multiple closest coords).
    grid = []
    exclusions = set([-1])
    for x in range(nmax.x):
        for y in range(nmax.y):
            pos = Coord(x, y)
            dists = list(map(lambda x: dist(pos, x), ncoords))
            counted = collections.Counter(dists)
            min_dist = min(dists)
            if counted[min_dist] == 1:
                grid.append(dists.index(min_dist))
            else:
                grid.append(-1)
            if x == 0 or y == 0 or x == nmax.x - 1 or y == nmax.y - 1:
                exclusions.add(grid[-1])

    # Determine candidate indices, and count occurrences of them. The largest
    # count is the size of the largest area.
    candidates = set(range(len(ncoords))) - exclusions
    counted = collections.Counter(grid)

    if len(candidates) < 1:
        return 0
    else:
        return counted[max(candidates, key=lambda i: counted[i])]

if __name__ == "__main__":
    solve(6, parse, largest_finite_area)
