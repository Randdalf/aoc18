#!/usr/bin/env python

"""Advent of Code 2018, Day 1, Puzzle 2"""

def solve(deltas):
    deltas = list(deltas)
    frequency = 0
    seen = set([frequency])
    while True:
        for delta in deltas:
            frequency += delta
            if frequency in seen:
                return frequency
            seen.add(frequency)

def sanitise(line):
    return int(line.strip())

def main():
    with open('d1.txt') as puzzle:
        print(solve(map(sanitise, puzzle.readlines())))

if __name__ == "__main__":
    main()
