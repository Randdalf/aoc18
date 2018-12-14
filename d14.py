#!/usr/bin/env python

"""Advent of Code 2018, Day 14"""

from aoc18 import solve

def parse(data):
    return int(data)

def digits(n):
    return map(int, str(n))

def step(recipes, elves):
    recipes.extend(digits(sum(map(lambda i: recipes[i], elves))))
    for i,elf in enumerate(elves):
        elves[i] = (elf + recipes[elf] + 1) % len(recipes)

def ten_scores_after_num(num):
    recipes = [3, 7]
    elves = [0, 1]
    while len(recipes) < num + 10:
        step(recipes, elves)
    return ''.join(map(str, recipes[num:num+10]))

def recipes_before_num(num):
    pattern = list(digits(num))
    recipes = [3, 7]
    elves = [0, 1]
    prev = 0
    while True:
        step(recipes, elves)
        curr = len(recipes) - len(pattern)
        for i in range(prev, curr):
            if recipes[i] == pattern[0] and all(map(lambda j: recipes[i+j] == pattern[j], range(1, len(pattern)))):
                return i
        prev = curr

if __name__ == "__main__":
    solve(14, parse, ten_scores_after_num, recipes_before_num)
