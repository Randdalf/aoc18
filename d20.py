#!/usr/bin/env python

"""Advent of Code 2018, Day 20"""

import re

from aoc18 import solve

def parse(data):
    return data[1:-1]

def north(room):
    return (room[0], room[1]-1)

def east(room):
    return (room[0]+1, room[1])

def south(room):
    return (room[0], room[1]+1)

def west(room):
    return (room[0]-1, room[1])

move = {'N':north, 'E':east, 'S':south, 'W':west}
cancel = {'N':'S', 'E':'W', 'S':'N', 'W':'E'}

def store(room, doors, min_doors):
    if room not in min_doors or min_doors[room] > doors:
        min_doors[room] = doors

def branch(input, i, room, doors, min_doors, skip):
    j = i
    parens = 1
    branches = [i]
    while parens > 0:
        c = input[j]
        if c == ')':
            parens -= 1
        elif c == '(':
            parens += 1
        elif c == '|' and parens == 1:
            branches.append(j+1)
        j += 1
    if branches[-1] + 1 == j:
        path(input, branches[0], room, doors, min_doors, skip + [len(input)])
        path(input, j, room, doors, min_doors, skip)
    else:
        for i in branches:
            if i == branches[-1]:
                path(input, i, room, doors, min_doors, skip)
            else:
                path(input, i, room, doors, min_doors, skip + [j])

def path(input, i, room, doors, min_doors, skip=[]):
    while i < len(input):
        c = input[i]
        if c == '(':
            branch(input, i+1, room, doors, min_doors, skip)
            return
        elif c == ')':
            i += 1
        elif c == '|':
            i = skip.pop()
        else:
            room = move[c](room)
            i += 1
            doors += 1
            store(room, doors, min_doors)

def most_doors_to_room(input):
    min_doors = {}
    path(input, 0, (0,0), 0, min_doors)
    return max(min_doors.values())

def rooms_at_least_1000_doors_away(input):
    min_doors = {}
    path(input, 0, (0,0), 0, min_doors)
    return sum([int(doors >= 1000) for doors in min_doors.values()])

if __name__ == "__main__":
    solve(20, parse, most_doors_to_room, rooms_at_least_1000_doors_away)
