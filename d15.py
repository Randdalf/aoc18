#!/usr/bin/env python

"""Advent of Code 2018, Day 15"""

from aoc18 import solve

class Vec2:
    def __init__(slf, x, y):
        slf.x = x
        slf.y = y

    def __add__(slf, otr):
        return Vec2(slf.x + otr.x, slf.y + otr.y)

    def __eq__(slf, otr):
        return slf.x == otr.x and slf.y == otr.y

    def __hash__(slf):
        return hash((slf.x, slf.y))

    def __repr__(slf):
        return f'({slf.x:3d}, {slf.y:3d})'

class World:
    def __init__(slf, size, units, walls):
        slf.size = size
        slf.units = units
        slf.walls = walls
        slf.rounds = 0

    def tick(slf):
        pass

    def __repr__(slf):
        if slf.rounds == 0:
            repr = 'Initially:\n'
        elif slf.rounds == 1:
            repr = 'After 1 round:\n'
        else:
            repr = f'After {slf.rounds} rounds:\n'
        units_by_pos = dict((u.pos, u) for u in slf.units)
        for y in range(slf.size.y):
            units_in_row = []
            for x in range(slf.size.x):
                pos = Vec2(x, y)
                if pos in slf.walls:
                    repr += '#'
                elif pos in units_by_pos:
                    unit = units_by_pos[pos]
                    repr += unit.faction
                    units_in_row.append(unit)
                else:
                    repr += '.'
            if len(units_in_row) > 0:
                repr += '   '
                repr += ', '.join(map(str, units_in_row))
            repr += '\n'
        return repr

class Unit:
    def __init__(slf, faction, pos):
        slf.faction = faction
        slf.pos = pos
        slf.hp = 200
        slf.atk = 3

    def __repr__(slf):
        return f'{slf.faction}({slf.hp})'

def parse(data):
    units = []
    walls = set()
    split = data.splitlines()
    size = Vec2(0, len(split))
    for y,line in enumerate(split):
        size.x = len(line)
        for x,c in enumerate(line):
            if c == '#':
                walls.add(Vec2(x, y))
            elif c == 'G' or c == 'E':
                units.append(Unit(c, Vec2(x, y)))
    return World(size, units, walls)

def simulate(world):
    print(world)

if __name__ == "__main__":
    solve(15, parse, simulate)
