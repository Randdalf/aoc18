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

def total_power(grid, x, y, sq):
    power = 0
    for j in range(0, sq):
        for i in range(0, sq):
            power += grid[index(x+i, y+j)]
    return power

def largest_total_power_3x3(serial):
    grid = calculate_power_grid(serial)

    # Find coord with largest total power level.
    largest_coord = None
    largest_power = None
    for y in range(size - 3):
        for x in range(size - 3):
            power = total_power(grid, x, y, 3)
            if largest_power is None or power > largest_power:
                largest_coord = (x+1, y+1)
                largest_power = power

    return largest_coord

def identifiers():
    for y in range(size):
        for x in range(size):
            for s in range(1, min(size - y, size - x)):
                yield(x + 1, y + 1, s)

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

def largest_total_power(serial):
    grid = calculate_power_grid(serial)
    sat = summed_area_table(grid)
    return max(identifiers(), key=lambda x: lookup_area(sat, x))

if __name__ == "__main__":
    solve(11, parse, largest_total_power_3x3, largest_total_power)
