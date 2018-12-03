#!/usr/bin/env python

"""Advent of Code 2018, Day 3 (Puzzle)"""

from aocd import get_data

class Rect:
    def __init__(slf, x, y, w, h):
        slf.l = x
        slf.r = x + w
        slf.t = y
        slf.b = y + h

def puzzle():
    for line in get_data(day=3, year=2018).split('\n'):
        parts = line.split('@')[1].split(':')
        pos = parts[0].strip().split(',')
        size = parts[1].strip().split('x')
        yield Rect(int(pos[0]), int(pos[1]), int(size[0]), int(size[1]))
