#!/usr/bin/env python

"""Advent of Code 2018, Day 22"""

import re
import math
from collections import defaultdict

from aoc18 import solve

# Region types.
ROCKY = 0
WET = 1
NARROW = 2

# Equipment types.
TORCH = 0
GEAR = 1
NEITHER = 2

# Contains valid pairs of region type and equipment, mapped to the equipment
# that is also valid in that region.
equipment = {
    (ROCKY, TORCH) : GEAR,
    (ROCKY, GEAR) : TORCH,
    (WET, GEAR) : NEITHER,
    (WET, NEITHER) : GEAR,
    (NARROW, TORCH) : NEITHER,
    (NARROW, NEITHER) : TORCH
}

class Cave:
    def __init__(slf, depth, target):
        slf.depth = depth
        slf.target = target
        slf.erosion = {}
        slf.types = {}

    def geologic(slf, x, y):
        if (x,y) == (0,0) or (x,y) == (slf.target[0], slf.target[1]):
            return 0
        elif y == 0:
            return x * 16807
        elif x == 0:
            return y * 48271
        else:
            return slf.erosion[(x-1,y)] * slf.erosion[(x,y-1)]

    def type(slf, x, y):
        region = (x, y)
        if region not in slf.types:
            e = (slf.geologic(x, y) + slf.depth) % 20183
            slf.erosion[region] = e
            slf.types[region] = e % 3
        return slf.types[region]

def parse(data):
    lines = data.splitlines()
    dp = re.compile('depth: (\d+)')
    tp = re.compile('target: (\d+),(\d+)')
    dm = re.match(dp, lines[0])
    tm = re.match(tp, lines[1])
    return Cave(int(dm.group(1)), (int(tm.group(1)), int(tm.group(2)), TORCH))

def risk_level(cave):
    w = cave.target[0] + 1
    h = cave.target[1] + 1
    return sum(cave.type(x, y) for x in range(w) for y in range(h))

def estimate_cost(f, t):
    return abs(f[0] - t[0]) + abs(f[1] - t[1])

def dist_between(f, t):
    return 7 if f[2] != t[2] else 1

hack = 15

def adjacencies(node, cave):
    if node[0] > 0:
        yield (node[0]-1, node[1])
    if node[1] > 0:
        yield (node[0], node[1]-1)
    # HACK: These should extend into infinity.
    if node[0] < cave.target[0] + hack - 1:
        yield (node[0]+1, node[1])
    if node[1] < cave.target[1] + hack - 1:
        yield (node[0], node[1]+1)

def neighbors(node, cave):
    type = cave.type(node[0], node[1])

    # Switching equipment.
    yield (node[0], node[1], equipment[(type, node[2])])

    # Moving to a valid adjacency.
    for x,y in adjacencies(node, cave):
        if (cave.type(x, y), node[2]) in equipment:
            yield (x, y, node[2])

def reconstruct_path(came_from, current, cave):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    mins = 0
    for i in range(1, len(path)):
        mins += dist_between(path[i-1], path[i])
    return mins

def shortest_path(cave):
    # HACK: Fill out the cave types ahead of time.
    for x in range(cave.target[0] + hack):
        for y in range(cave.target[1] + hack):
            cave.type(x, y)

    # A* search algorithm.
    start = (0,0,TORCH)
    closed = set()
    open = {start}
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0
    f_score = defaultdict(lambda: math.inf)
    f_score[start] = estimate_cost(start, cave.target)
    while len(open) > 0:
        # OPTIMISATION: Use priority queue.
        current = min(open, key=lambda x: f_score[x])
        if current == cave.target:
            return reconstruct_path(came_from, current, cave)
        open.remove(current)
        closed.add(current)
        for neighbor in neighbors(current, cave):
            if neighbor in closed:
                continue
            tentative_g = g_score[current] + dist_between(current, neighbor)
            if neighbor not in open:
                open.add(neighbor)
            elif tentative_g >= g_score[neighbor]:
                continue
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g
            f_score[neighbor] = tentative_g + estimate_cost(neighbor, cave.target)

if __name__ == "__main__":
    solve(22, parse, risk_level, shortest_path)
