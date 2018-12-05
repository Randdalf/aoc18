#!/usr/bin/env python

"""Advent of Code 2018"""

import aocd
from time import perf_counter

def run_solver(day, level, solver, input):
    start = perf_counter()
    answer = solver(input)
    end = perf_counter()
    print('{0:<30} ({1:.4f}s)'.format(answer, end - start))

def solve(day, parse, *solvers):
    data = aocd.get_data(day=day, year=2018)
    for i, solver in enumerate(solvers):
        run_solver(day, i+1, solver, parse(data))
