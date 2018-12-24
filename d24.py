#!/usr/bin/env python

"""Advent of Code 2018, Day 24"""

import re
from itertools import islice

from aoc18 import solve

class Group:
    def __init__(slf, id, army, units, hp, atk, atk_type, initiative, immune, weak):
        slf.id = id
        slf.army = army
        slf.units = units
        slf.hp = hp
        slf.atk = atk
        slf.atk_type = atk_type
        slf.initiative = initiative
        slf.immune = immune
        slf.weak = weak

    def power(slf):
        return slf.units * slf.atk

def parse(data):
    groups = []
    blocks = data.split('\n\n')
    group_pattern = re.compile('(?P<units>\d+) units each with (?P<hp>\d+) hit points( \((?P<attrs>[\w;, ]+)\))? with an attack that does (?P<atk>\d+) (?P<atk_type>\w+) damage at initiative (?P<initiative>\d+)')
    for block in blocks:
        lines = block.splitlines()
        army = lines[0].split(':')[0]
        for id,line in enumerate(islice(lines, 1, None), 1):
            m = re.match(group_pattern, line).groupdict()
            units = int(m['units'])
            hp = int(m['hp'])
            attrs = m['attrs']
            immune = set()
            weak = set()
            if attrs:
                for part in m['attrs'].split('; '):
                    bits = part.split('to ')
                    bobs = bits[1].split(', ')
                    if bits[0].startswith('immune'):
                        immune.update(bobs)
                    elif bits[0].startswith('weak'):
                        weak.update(bobs)
            atk = int(m['atk'])
            atk_type = m['atk_type']
            initiative = int(m['initiative'])
            groups.append(Group(id, army, units, hp, atk, atk_type, initiative, immune, weak))
    return groups

def damage(attacker, defender):
    if attacker.atk_type in defender.immune:
        return 0
    elif attacker.atk_type in defender.weak:
        return 2 * attacker.power()
    else:
        return attacker.power()

def print_state(groups):
    for army in ['Immune System', 'Infection']:
        print(f'{army}:')
        army_groups = list(filter(lambda g: g.army == army, groups))
        if len(army_groups) > 0:
            for group in sorted(army_groups, key=lambda g: g.id):
                print('Group', group.id, 'contains', group.units, 'units')
        else:
            print('No groups remain.')

def fight(groups, verbose=True):
    # Print out the current state.
    if verbose:
        print_state(groups)
        print()

    # Target selection phase.
    groups.sort(key=lambda g:(g.power(), g.initiative), reverse=True)
    available = set(groups)
    for attacker in groups:
        attacker.target = None
        targets = list(filter(lambda t: t.army != attacker.army, available))
        if len(targets) > 0:
            targets.sort(key=lambda d:(damage(attacker, d), d.power(), d.initiative), reverse=True)
            for target in targets:
                dmg = damage(attacker, target)
                if verbose: print(f'{attacker.army} group {attacker.id} would deal defending group {target.id} {dmg} damage')
            if damage(attacker, targets[0]) > 0:
                attacker.target = targets[0]
                available.remove(attacker.target)

    if verbose: print()

    # Attacking phase.
    groups.sort(key=lambda g:g.initiative, reverse=True)
    for attacker in groups:
        defender = attacker.target
        if defender and attacker.units > 0:
            dmg = damage(attacker, defender)
            before = defender.units
            defender.units = max(defender.units - dmg // defender.hp, 0)
            killed = before - defender.units
            if verbose: print(f'{attacker.army} group {attacker.id} attacks defending group {defender.id}, killing {killed} units')

    if verbose: print()

    # Remove all groups without any units left.
    for group in list(groups):
        if group.units == 0:
            groups.remove(group)

    # Tidying up.
    for group in groups:
        del group.target

def simulate(groups, verbose=False):
    while len(set(map(lambda g: g.army, groups))) > 1:
        fight(groups, verbose)
    if verbose:
        print_state(groups)
    return sum(g.units for g in groups)

if __name__ == "__main__":
    solve(24, parse, simulate)
