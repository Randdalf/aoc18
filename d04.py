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

class SleepyGuard:
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

def get_guards_from_shifts(shifts):
    guards = {}
    for shift in shifts:
        if shift.guard_id not in guards:
            guards[shift.guard_id] = SleepyGuard(shift.guard_id)
        guard = guards[shift.guard_id]

        for i in range(0, len(shift.events), 2):
            guard.add_sleep(shift.events[i], shift.events[i+1])
    return guards.values()

def find_sleepiest_guard_1(shifts):
    guards = get_guards_from_shifts(shifts)
    sleepiest_guard = max(guards, key=lambda x: x.total_sleep())
    return sleepiest_guard.id * sleepiest_guard.sleepiest_minute()

def find_sleepiest_guard_2(shifts):
    guards = get_guards_from_shifts(shifts)
    max_sleep = None
    max_guard = None
    max_minute = None
    for minute in range(60):
        for guard in guards:
            sleep = guard.minutes[minute]
            if not max_sleep or sleep > max_sleep:
                max_sleep = sleep
                max_guard = guard
                max_minute = minute
    return max_guard.id * max_minute

if __name__ == "__main__":
    solve(4, parse, find_sleepiest_guard_1, find_sleepiest_guard_2)
