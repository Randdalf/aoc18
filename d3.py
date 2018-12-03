#!/usr/bin/env python

"""Advent of Code 2018, Day 3 (Puzzle)"""

from aocd import get_data

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

def puzzle():
    for line in get_data(day=3, year=2018).split('\n'):
        parts = line.split('@')
        id = parts[0].split('#')[1]
        rectParts = parts[1].split(':')
        pos = rectParts[0].strip().split(',')
        size = rectParts[1].strip().split('x')
        yield Rect(int(id), int(pos[0]), int(pos[1]), int(size[0]), int(size[1]))
