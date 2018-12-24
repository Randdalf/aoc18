#!/usr/bin/env python

"""Advent of Code 2018, Day 15"""

import math
import cProfile
from copy import deepcopy
from pqueue import pqueue

from aoc18 import solve

class Unit:
    def __init__(slf, faction, pos):
        slf.faction = faction
        slf.pos = pos
        slf.hp = 200
        slf.atk = 3

    def __repr__(slf):
        return f'{slf.faction}({slf.hp})'

def adjacencies(pos):
    # Adjacencies are intentionally returned in reading order, so we only have
    # to calculate a single shortest path to each target.
    y = pos[0]
    x = pos[1]
    yield (y-1,x)
    yield (y,x-1)
    yield (y,x+1)
    yield (y+1,x)

def shortest_path_prev(source, verts):
    # Initialisation.
    q = pqueue()
    dist = {v: math.inf for v in verts}
    prev = {v: None for v in verts}
    dist[source] = 0
    for v in verts:
        q.add(v, dist[v])

    # Work out dist and prev for each vertex.
    while len(q) > 0:
        u = q.pop()
        for v in adjacencies(u):
            if v in q:
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    q.add(v, alt)

    return prev

def shortest_path(source, target, prev):
    # Working backwards, find the shortest path from source to target.
    path = []
    u = target
    if prev[u] or u == source:
        while u:
            path.append(u)
            u = prev[u]

    return (path[-2], len(path)) if len(path) > 0 else None

class World:
    def __init__(slf, width, height, units, walls):
        slf.width = width
        slf.height = height
        slf.units = units
        slf.walls = walls
        slf.rounds = 0
        slf.winner = None
        slf.done = False
        slf.terminate_on_elf_death = False
        slf.all = set((y, x) for y in range(slf.height) for x in range(slf.width))

    def modify_elf_atk(slf, new_atk):
        for unit in slf.units:
            if unit.faction == 'E':
                unit.atk = new_atk

    def tick(slf):
        # If we're finishing simulating combat, then don't tick.
        if slf.done:
            return

        dead = set()

        # Units take turns in reading order.
        for unit in sorted(slf.units, key=lambda u:u.pos):
            # Dead men take no turns.
            if unit in dead:
                continue

            # Identify all targets.
            targets = list(filter(lambda u: u.faction != unit.faction, slf.units))

            # If this unit finds no targets, end the simulation.
            if len(targets) == 0:
                slf.winner = unit.faction
                slf.done = True
                return

            # Identify all open squares in range of each target. A unit ends its
            # turn if there are no open in-range squares and it is not in-range
            # of the target.
            closed = slf.walls | set(u.pos for u in slf.units)
            all_in_range = set(adj for t in targets for adj in adjacencies(t.pos))
            open_in_range = list(filter(lambda x: x not in closed, all_in_range))

            # Sort open in range by reading order.
            open_in_range.sort()

            # If we're not in-range of a target, then move.
            if unit.pos not in all_in_range:

                # If there are no in-range targets, then we can't do anything.
                if len(open_in_range) == 0:
                    continue

                # Find the shortest open paths to each open in-range square.
                # These should be in reading order, due to the ordering of the
                # in-range targets, graph vertices, and adjacencies.
                open = slf.all - closed
                verts = sorted(open | set([unit.pos]))
                prev = shortest_path_prev(unit.pos, verts)
                all_paths = [shortest_path(unit.pos, t, prev) for t in open_in_range]
                open_paths = [p for p in all_paths if p]

                # If there are no open paths, then end our turn.
                if len(open_paths) == 0:
                    continue

                # Move to the first square on the shortest path.
                unit.pos = min(open_paths, key=lambda x: x[1])[0]

            # If we're in range of a target, then attack.
            if unit.pos in all_in_range:
                danger = set(adjacencies(unit.pos))
                adj_targets = filter(lambda t: t.pos in danger, targets)
                adj_targets = sorted(adj_targets, key=lambda t: (t.hp, t.pos))
                atk_target = adj_targets[0]
                atk_target.hp -= unit.atk
                if atk_target.hp <= 0:
                    slf.units.remove(atk_target)
                    dead.add(atk_target)

                    # Stop ticking if an elf dies and that is undesirable.
                    if slf.terminate_on_elf_death and atk_target.faction == 'E':
                        slf.done = True
                        return

        # We have finished a round.
        slf.rounds += 1

    def outcome(slf):
        return slf.rounds * sum(unit.hp for unit in slf.units)

    def __repr__(slf):
        if slf.rounds == 0:
            repr = 'Initially:\n'
        elif slf.rounds == 1:
            repr = 'After 1 round:\n'
        else:
            repr = f'After {slf.rounds} rounds:\n'
        units_by_pos = dict((u.pos, u) for u in slf.units)
        for y in range(slf.height):
            units_in_row = []
            for x in range(slf.width):
                pos = (y, x)
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

def parse(data):
    units = []
    walls = set()
    split = data.splitlines()
    height = len(split)
    for y,line in enumerate(split):
        width = len(line)
        for x,c in enumerate(line):
            if c == '#':
                walls.add((y, x))
            elif c == 'G' or c == 'E':
                units.append(Unit(c, (y, x)))
    return World(width, height, units, walls)

def simulate(world, elf_atk, verbose):
    if elf_atk:
        world.modify_elf_atk(elf_atk)
        if verbose:
            print('Elf attack modified to', elf_atk)
    if verbose:
        print(world)
    while not world.done:
        world.tick()
        if verbose:
            print(world)
    return world

def default_outcome(world, verbose=False):
    simulate(world, None, verbose)
    return world.outcome()

def elves_win_outcome(orig_world, verbose=False):
    atk = 3
    world = None
    orig_world.terminate_on_elf_death = True

    while not world or world.winner != 'E':
        world = simulate(deepcopy(orig_world), atk, verbose)
        atk += 1

    return world.outcome()

if __name__ == "__main__":
    solve(15, parse, default_outcome, elves_win_outcome)
