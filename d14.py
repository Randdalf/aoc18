#!/usr/bin/env python

"""Advent of Code 2018, Day 14"""

from aoc18 import solve

def parse(data):
    return int(data)

def rdigits(n):
    if n == 0:
        yield 0
    else:
        while n > 0:
            yield n % 10
            n //= 10

def digits(n):
    return reversed(list(rdigits(n)))

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

if __name__ == "__main__":
    solve(14, parse, ten_scores_after_num)
