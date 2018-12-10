#!/usr/bin/env python

"""Advent of Code 2018, Day 10"""

import re
import functools

from aoc18 import solve

class Vector2:
    def __init__(slf, x, y):
        slf.x = x
        slf.y = y

    def __add__(slf, otr):
        return Vector2(slf.x + otr.x, slf.y + otr.y)

    def __sub__(slf, otr):
        return Vector2(slf.x - otr.x, slf.y - otr.y)

def scale(v, k):
    return Vector2(v.x * k, v.y * k)

def vmax(a, b):
    return Vector2(max(a.x, b.x), max(a.y, b.y))

def vmin(a, b):
    return Vector2(min(a.x, b.x), min(a.y, b.y))

class Light:
    def __init__(slf, p, v):
        slf.p = p
        slf.v = v

def make_light(px, py, vx, vy):
    return Light(Vector2(px, py), Vector2(vx, vy))

def parse(data):
    pattern = re.compile("position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>")
    return [make_light(*map(int, re.match(pattern, line).groups())) for line in data.splitlines()]

def bounds(lights):
    min = functools.reduce(vmin, map(lambda x: x.p, lights))
    max = functools.reduce(vmax, map(lambda x: x.p, lights))
    return (min, max)

def simulate(lights, t):
    for light in lights:
        yield Light(light.p + scale(light.v, t), light.v)

def entropy(lights):
    min, max = bounds(lights)
    size = max - min
    return size.x * size.y

def generate_moves():
    for s in [-1, +1]:
        for k in range(14):
            yield s * 2 ** k

def seconds_to_message(lights):
    moves = list(generate_moves())
    min_entropy = entropy(lights)
    seconds = 0

    while True:
        entropies = [entropy(list(simulate(lights, seconds + move))) for move in moves]
        min_index = min(range(len(entropies)), key=lambda i: entropies[i])

        if entropies[min_index] < min_entropy:
            min_entropy = entropies[min_index]
            seconds += moves[min_index]
        else:
            return seconds

def spell_message(lights):
    seconds = seconds_to_message(lights)
    lights = list(simulate(lights, seconds))
    bmin, bmax  = bounds(lights)
    size = bmax - bmin
    points = set([(v.x, v.y) for v in map(lambda l: l.p - bmin, lights)])
    chars = []

    for y in range(size.y+1):
        for x in range(size.x+1):
                if (x, y) in points:
                    chars.append("#")
                else:
                    chars.append(".")
        chars.append('\n')

    return ''.join(chars)

if __name__ == "__main__":
    solve(10, parse, spell_message, seconds_to_message)
