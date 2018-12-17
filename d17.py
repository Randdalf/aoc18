#!/usr/bin/env python

"""Advent of Code 2018, Day 17"""

import re
import png

from aoc18 import solve

def parse(data):
    x_pattern = re.compile('x=(\d+), y=(\d+)\.\.(\d+)')
    y_pattern = re.compile('y=(\d+), x=(\d+)\.\.(\d+)')
    state = {}
    for line in data.splitlines():
        if line.startswith('x'):
            nums = [int(k) for k in re.match(x_pattern, line).groups()]
            for y in range(nums[1], nums[2]+1):
                state[(nums[0], y)] = '#'
        else:
            nums = [int(k) for k in re.match(y_pattern, line).groups()]
            for x in range(nums[1], nums[2]+1):
                state[(x, nums[0])] = '#'
    return state

def left(pos):
    return (pos[0] - 1, pos[1])

def right(pos):
    return (pos[0] + 1, pos[1])

def down(pos):
    return (pos[0], pos[1] + 1)

def write_png(state, stream, spring):
    min_x = min(p[0] for p in state) - 1
    max_x = max(p[0] for p in state) + 2
    min_y = min(p[1] for p in state) - 1
    max_y = max(p[1] for p in state) + 2
    w = max_x - min_x
    h = max_y - min_y

    with open('d17.png', 'wb') as f:
        writer = png.Writer(w, h)
        pixels = []
        for y in range(min_y, max_y):
            row = []
            for x in range(min_x, max_x):
                pos = (x, y)
                if pos == spring:
                    row.extend([0, 0, 128])
                elif pos in state:
                    if state[pos] == '#':
                        row.extend([255, 255, 255])
                    elif state[pos] == '~':
                        row.extend([128, 128, 255])
                elif pos in stream:
                    row.extend([0, 0, 255])
                else:
                    row.extend([0, 0, 0])
            pixels.append(row)
        writer.write(f, pixels)

def simulate_stream(state):
    spring = (500, 0)
    min_y = min(p[1] for p in state)
    max_y = max(p[1] for p in state)

    # Move the spring down until it's within the bounds.
    while down(spring)[1] < min_y:
        spring = down(spring)

    # Simulate the water until no water settles in a pass.
    settled = True
    while settled:
        sources = [spring]
        to_settle = set()
        stream = set()

        while len(sources) > 0:
            # Move down until we encounter a blockage.
            w = sources.pop()
            while down(w) not in state and down(w) not in stream and down(w)[1] <= max_y:
                w = down(w)
                stream.add(w)

            # Stop simulating from this source if we are outside the bounds, or
            # we've already simulated from this tile.
            if w[1] == 0 or down(w)[1] > max_y or down(w) in stream:
                continue

            # Spread left and right.
            l = w
            while down(l) in state and left(l) not in state and left(l) not in stream:
                l = left(l)
                stream.add(l)

            r = w
            while down(r) in state and right(r) not in state and right(r) not in stream:
                r = right(r)
                stream.add(r)

            # Check if we should settle.
            if down(l) in state and down(r) in state and left(l) in state and right(r) in state:
                for x in range(l[0], r[0]+1):
                    to_settle.add((x, l[1]))
            # Otherwise, check if we should spawn new streams.
            else:
                if down(l) not in state and down(l) not in stream:
                    sources.append(l)
                if down(r) not in state and down(r) not in stream:
                    sources.append(r)

        settled = len(to_settle) > 0
        for s in to_settle:
            state[s] = '~'

    write_png(state, stream, spring)

    return stream

def count_all_water(state):
    stream = simulate_stream(state)
    return len(stream) + sum(int(s == '~') for s in state.values())

def count_settled_water(state):
    stream = simulate_stream(state)
    return sum(int(s == '~') for s in state.values())

if __name__ == "__main__":
    solve(17, parse, count_all_water, count_settled_water)
