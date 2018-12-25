#!/usr/bin/env python

"""Advent of Code 2018, Day 25"""

from aoc18 import solve

def parse(data):
    return {tuple(int(x) for x in line.split(',')) for line in data.splitlines()}

def dist(a, b):
    return sum(abs(n-m) for n,m in zip(a,b))

def num_constellations(points):
    constellations = []
    while len(points) > 0:
        expanded = set()
        unexpanded = {points.pop()}
        while len(unexpanded) > 0:
            pt = unexpanded.pop()
            neighbors = {n for n in points if dist(pt, n) <= 3}
            points -= neighbors
            unexpanded |= neighbors
            expanded.add(pt)
        constellations.append(expanded)
    return len(constellations)

if __name__ == "__main__":
    solve(25, parse, num_constellations)
