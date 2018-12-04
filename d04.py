#!/usr/bin/env python

"""Advent of Code 2018, Day 4"""

import re

from aoc18 import solve

class Shift:
    def __init__(slf, guard_id):
        slf.guard_id = guard_id
        slf.events = []

def parse(data):
    shifts = []
    shift = None
    pattern = re.compile("\[\d+-\d+-\d+ \d+:(?P<min>\d+)\] (?:wakes up|falls asleep|Guard #(?P<guard_id>\d+) begins shift)")
    for record in sorted(data.split('\n')):
        match = re.match(pattern, record)
        guard_id = match.group('guard_id')
        if guard_id:
            shift = Shift(int(guard_id))
            shifts.append(shift)
        else:
            shift.events.append(int(match.group('min')))
    return shifts

class Guard:
    def __init__(slf, id):
        slf.id = id
        slf.minutes = [0 for i in range(60)]

    def add_sleep(slf, start, end):
        for i in range(start, end):
            slf.minutes[i] += 1

    def total_sleep(slf):
        return sum(slf.minutes)

    def sleepiest_minute(slf):
        return max(range(60), key=lambda x: slf.minutes[x])

def find_sleepiest_guard(shifts):
    guards = {}
    for shift in shifts:
        if shift.guard_id not in guards:
            guards[shift.guard_id] = Guard(shift.guard_id)
        guard = guards[shift.guard_id]

        for i in range(0, len(shift.events), 2):
            guard.add_sleep(shift.events[i], shift.events[i+1])

    sleepiest_guard = max(guards.values(), key=lambda x: x.total_sleep())
    return sleepiest_guard.id * sleepiest_guard.sleepiest_minute()

if __name__ == "__main__":
    solve(4, parse, find_sleepiest_guard)
