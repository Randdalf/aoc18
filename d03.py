#!/usr/bin/env python

"""Advent of Code 2018, Day 3"""

import re
from collections import Counter

from aoc18 import solve

class Rect:
    def __init__(slf, id, x, y, w, h):
        slf.id  = id
        slf.l = x
        slf.r = x + w
        slf.t = y
        slf.b = y + h

    def squares(slf):
        for x in range(slf.l, slf.r):
            for y in range(slf.t, slf.b):
                yield (x, y)

def parse(data):
    pattern = re.compile("#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)")
    for line in data.split('\n'):
        yield Rect(*map(int, re.match(pattern, line).groups()))

def get_all_squares(rects):
    for rect in rects:
        yield from rect.squares()

def accumulate_occupancy(rects):
    return Counter(get_all_squares(rects))

def count_occupied_squares(rects):
    return sum(map(lambda x: int(x >= 2), accumulate_occupancy(rects).values()))

def find_rect_without_overlaps(rects):
    rects = list(rects)
    occupancy = accumulate_occupancy(rects)
    for r in rects:
        if all(map(lambda x: occupancy[x] == 1, r.squares())):
            return r.id

if __name__ == "__main__":
    solve(3, parse, count_occupied_squares, find_rect_without_overlaps)
