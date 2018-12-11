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
            for sq in range(1, min(size - y, size - x)):
                yield(x, y, sq)
                
def largest_total_power(serial):
    grid = calculate_power_grid(serial)
    totals = [0 for _ in range(len(grid))]
    identifier = None
    largest_power =  None
    for sq in range(size):
        limit = size - sq

        # Increment totals.
        for y in range(0, limit):
            for x in range(0, limit):
                power = 0
                for i in range(0, sq+1):
                    power += grid[index(x+i, y+sq)]
                for j in range(0, sq):
                    power += grid[index(x+sq, y+j)]
                totals[index(x,y)] += power

        # Find identifier with largest total power.
        for y in range(0, limit):
            for x in range(0, limit):
                power = totals[index(x, y)]
                if not largest_power or power > largest_power:
                    largest_power = power
                    identifer = (x+1,y+1,sq+1)

    return identifer

if __name__ == "__main__":
    solve(11, parse, largest_total_power_3x3, largest_total_power)
