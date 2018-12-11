#!/usr/bin/env python

"""Advent of Code 2018, Day 11"""

from aoc18 import solve

size=(300,300)
square=(3,3)

def parse(data):
    return int(data)

def power_level(x, y, serial):
    rid = x + 10
    return ((rid * (y * rid + serial)) // 100) % 10 - 5

def calculate_power_grid(serial):
    grid = []
    for y in range(1, size[1]+1):
        for x in range(1, size[0]+1):
            grid.append(power_level(x, y, serial))
    return grid

def largest_total_power(serial):
    grid = calculate_power_grid(serial)

    # Find coord with largest total power level.
    index = 0
    largest_coord = None
    largest_power = None
    for y in range(size[1] - square[1]):
        for x in range(size[0] - square[0]):
            power = 0
            for j in range(0, square[1]):
                for i in range(0, square[0]):
                    power += grid[(y + j)*size[1] + x + i]
            if largest_power is None or power > largest_power:
                largest_coord = (x+1, y+1)
                largest_power = power

    return largest_coord

if __name__ == "__main__":
    solve(11, parse, largest_total_power)
