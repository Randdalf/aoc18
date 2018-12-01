#!/usr/bin/env python

"""Advent of Code 2018, Day 1, Puzzle 1"""

def solve(frequencies):
    return sum(frequencies)

def sanitise(line):
    return int(line.strip())

def main():
    with open('d1p1.txt') as puzzle:
        print(solve(map(sanitise, puzzle.readlines())))

if __name__ == "__main__":
    main()
