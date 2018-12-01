#!/usr/bin/env python

"""Advent of Code 2018, Day 1 (Puzzle)"""

from aocd import get_data

def puzzle():
    return map(int, get_data(day=1, year=2018).split('\n'))
