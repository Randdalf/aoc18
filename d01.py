#!/usr/bin/env python

"""Advent of Code 2018, Day 1"""

from aoc18 import solve

def parse(data):
    return map(int, data.split('\n'))

def sum_deltas(deltas):
    return sum(deltas)

def find_repeated_freq(deltas):
    deltas = list(deltas)
    frequency = 0
    seen = set()
    while True:
        for delta in deltas:
            seen.add(frequency)
            frequency += delta
            if frequency in seen:
                return frequency

if __name__ == "__main__":
    solve(1, parse, sum_deltas, find_repeated_freq)
