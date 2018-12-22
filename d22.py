#!/usr/bin/env python

"""Advent of Code 2018, Day 22"""

import re
import math
import itertools
from collections import defaultdict
from heapq import heappush
from heapq import heappop

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
        if (x,y) == (0,0) or (x,y) == slf.target:
            return 0
        elif y == 0:
            return x * 16807
        elif x == 0:
            return y * 48271
        else:
            # Ensure we have the erosion values calculated.
            slf.type(x-1,y)
            slf.type(x,y-1)
            return slf.erosion[(x-1,y)] * slf.erosion[(x,y-1)]

    def type(slf, x, y):
        region = (x, y)
        if region not in slf.types:
            e = (slf.geologic(x, y) + slf.depth) % 20183
            slf.erosion[region] = e
            slf.types[region] = e % 3
        return slf.types[region]

class pqueue:
    def __init__(slf):
        slf.pq = []
        slf.finder = {}
        slf.counter = itertools.count()
        slf.n = 0

    def add(slf, task, priority):
        if task in slf.finder:
            slf.remove(task)
        entry = [priority, next(slf.counter), task]
        slf.finder[task] = entry
        heappush(slf.pq, entry)
        slf.n += 1

    def remove(slf, task):
        entry = slf.finder.pop(task)
        entry[-1] = None
        slf.n -= 1

    def pop(slf):
        while slf.pq:
            priority, count, task = heappop(slf.pq)
            if task:
                del slf.finder[task]
                return task

    def __len__(slf):
        return slf.n

    def __contains__(slf, task):
        return task in slf.finder

def parse(data):
    lines = data.splitlines()
    dp = re.compile('depth: (\d+)')
    tp = re.compile('target: (\d+),(\d+)')
    dm = re.match(dp, lines[0])
    tm = re.match(tp, lines[1])
    return Cave(int(dm.group(1)), (int(tm.group(1)), int(tm.group(2))))

def risk_level(cave):
    w = cave.target[0] + 1
    h = cave.target[1] + 1
    return sum(cave.type(x, y) for x in range(w) for y in range(h))

def estimate_cost(f, t):
    return abs(f[0] - t[0]) + abs(f[1] - t[1])

def dist_between(f, t):
    return 7 if f[2] != t[2] else 1

def adjacencies(node, cave):
    if node[0] > 0:
        yield (node[0]-1, node[1])
    if node[1] > 0:
        yield (node[0], node[1]-1)
    yield (node[0]+1, node[1])
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
    # A* search algorithm.
    start = (0,0,TORCH)
    sink = (*cave.target,TORCH)
    closed = set()
    open = pqueue()
    open.add(start, estimate_cost(start, sink))
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0
    while len(open) > 0:
        current = open.pop()
        if current == sink:
            return reconstruct_path(came_from, current, cave)
        closed.add(current)
        for neighbor in neighbors(current, cave):
            if neighbor in closed:
                continue
            tentative_g = g_score[current] + dist_between(current, neighbor)
            if neighbor in open and tentative_g >= g_score[neighbor]:
                continue
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g
            open.add(neighbor, tentative_g + estimate_cost(neighbor, sink))

if __name__ == "__main__":
    solve(22, parse, risk_level, shortest_path)
