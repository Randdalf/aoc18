#!/usr/bin/env python

"""Advent of Code 2018, Day 7"""

import re
import operator
import itertools
import collections

from aoc18 import solve

def parse(data):
    pattern = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
    return [re.match(pattern, line).groups() for line in data.splitlines()]

def process_work(instructions):
    outputs = collections.defaultdict(list)
    for a,b in instructions:
        outputs[a].append(b)

    outstanding = collections.defaultdict(int)
    for b,a in map(reversed, instructions):
        outstanding[b] += 1

    steps = sorted(list(set(itertools.chain.from_iterable(instructions))))

    return (outputs, outstanding, steps)

def work_order(instructions):
    outputs, outstanding, steps = process_work(instructions)
    order = []
    while len(steps) > 0:
        step = next(filter(lambda x: x == 0, steps), None)
        step = next(x for x in steps if outstanding[x] == 0)
        steps.remove(step)
        order.append(step)
        for output in outputs[step]:
            outstanding[output] -= 1

    return ''.join(order)

def work_time(instructions, base_duration, throughput):
    outputs, outstanding, steps = process_work(instructions)
    active_steps = {}
    time = 0
    while len(steps) or len(active_steps) > 0:
        # Check if steps are complete.
        done_steps = []
        for step in active_steps:
            time_left = active_steps[step] - 1;
            if time_left > 0:
                active_steps[step] = time_left
            else:
                done_steps.append(step)
                for output in outputs[step]:
                    outstanding[output] -= 1
        # Remove done steps. (Can't do this whilst iterating over dict.)
        for step in done_steps:
            del active_steps[step]
        # Assign steps to workers.
        while len(active_steps) < throughput:
            step = next(filter(lambda x: outstanding[x] == 0, steps), None)
            if not step:
                break
            steps.remove(step)
            active_steps[step] = base_duration + ord(step) - ord('A') + 1
        time += 1
    return time - 1

def work_time_60_5(instructions):
    return work_time(instructions, 60, 5)

if __name__ == "__main__":
    solve(7, parse, work_order, work_time_60_5)
