#!/usr/bin/env python

"""Advent of Code 2018, Day 11"""

from aoc18 import solve

size = 300

def parse(data):
    return int(data)

def power_level(x, y, serial):
    rid = x + 10
    return ((rid * (y * rid + serial)) // 100) % 10 - 5

def calculate_power_grid(serial):
    grid = []
    for y in range(1, size+1):
        for x in range(1, size+1):
            grid.append(power_level(x, y, serial))
    return grid

def index(x, y):
    return y * size + x

def identifiers(low, high):
    for y in range(size):
        for x in range(size):
            for s in range(low, high+1):
                if x + s < size and y + s < size:
                    yield(x+1, y+1, s)

def summed_area_table(grid):
    table = []
    for y in range(size):
        for x in range(size):
            sum = grid[index(x,y)]
            if x > 0:
                sum += table[index(x-1,y)]
            if y > 0:
                sum += table[index(x, y-1)]
            if x > 0 and y > 0:
                sum -= table[index(x-1, y-1)]
            table.append(sum)
    return table

def lookup_area(sat, id):
    l = id[0]-2
    r = l+id[2]
    t = id[1]-2
    b = t+id[2]
    sa = sat[index(l, t)] if l >= 0 and t >= 0 else 0
    sb = sat[index(r, t)] if t >= 0 else 0
    sc = sat[index(l, b)] if l >= 0 else 0
    sd = sat[index(r, b)]
    return sd + sa - sb - sc

def largest_total_power(serial, low, high):
    grid = calculate_power_grid(serial)
    sat = summed_area_table(grid)
    return max(identifiers(low, high), key=lambda x: lookup_area(sat, x))

if __name__ == "__main__":
    solver1 = lambda x: largest_total_power(x, 3, 3)[:2]
    solver2 = lambda x: largest_total_power(x, 1, 300)
    solve(11, parse, solver1, solver2)
