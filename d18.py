#!/usr/bin/env python

"""Advent of Code 2018, Day 18"""

from aoc18 import solve

# 0 - . (open)
# 1 - | (trees)
# 2 - # (lumberyard)
# 3 -   (buffer)
code = { '.' : 0, '|' : 1, '#' : 2, ' ' : 3}
inv = {k:v for v,k in code.items()}

class Area:
    def __init__(slf, tiles, size):
        slf.tiles = tiles
        slf.size = size
        slf.offsets = [
            -size-1,
            -size,
            -size+1,
            -1,
            +1,
            size-1,
            size,
            size+1
        ]

def parse(data):
    tiles = []
    lines = data.splitlines()
    size = len(lines[0]) + 2
    tiles.extend(3 for _ in range(size))
    for line in data.splitlines():
        tiles.append(3)
        for c in line:
            tiles.append(code[c])
        tiles.append(3)
    tiles.extend(3 for _ in range(size))
    return Area(tiles, size)

def print_area(area):
    t = ''
    index = 0
    for y in range(area.size):
        for x in range(area.size):
            t += inv[area.tiles[index]]
            index += 1
        t += '\n'
    print(t)

def simulate(area, minutes):
    for m in range(minutes):
        index = area.size
        new_tiles = []
        new_tiles.extend(3 for _ in range(area.size))
        for y in range(1, area.size - 1):
            new_tiles.append(3)
            index += 1
            for x in range(0, area.size - 2):
                tile = area.tiles[index]
                counts = [0, 0, 0, 0]
                for offset in area.offsets:
                    counts[area.tiles[index + offset]] += 1
                if tile == 0:
                    if counts[1] >= 3:
                        new_tiles.append(1)
                    else:
                        new_tiles.append(0)
                elif tile == 1:
                    if counts[2] >= 3:
                        new_tiles.append(2)
                    else:
                        new_tiles.append(1)
                elif tile == 2:
                    if counts[1] >= 1 and counts[2] >= 1:
                        new_tiles.append(2)
                    else:
                        new_tiles.append(0)
                index += 1
            new_tiles.append(3)
            index += 1
        new_tiles.extend(3 for _ in range(area.size))
        area.tiles = new_tiles

def calculate_value(area):
    counts = [0, 0, 0, 0]
    for tile in area.tiles:
        counts[tile] += 1
    return counts[1] * counts[2]

def resource_value(area, minutes):
    if minutes < 500:
        simulate(area, minutes)
        return calculate_value(area)

    seen = {}
    for m in range(1, minutes + 1):
        simulate(area, 1)
        checksum = hash(tuple(area.tiles))
        if checksum not in seen:
            seen[checksum] = m
        else:
            cycle = m - seen[checksum]
            lookahead = (minutes - m) % cycle
            simulate(area, lookahead)
            return calculate_value(area)

if __name__ == "__main__":
    solve(18, parse, lambda x: resource_value(x, 10), lambda x: resource_value(x, 1000000000))
