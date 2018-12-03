#!/usr/bin/env python

"""Advent of Code 2018"""

import aocd

def run_solver(day, level, solver, input):
    print(solver(input))

def solve(day, parse, *solvers):
    data = aocd.get_data(day=day, year=2018)
    for i, solver in enumerate(solvers):
        run_solver(day, i+1, solver, parse(data))
