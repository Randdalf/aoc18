#!/usr/bin/env python

"""Advent of Code 2018, Day 13"""

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
        return str((slf.x, slf.y))

class Madness:
    def __init__(slf, tracks, carts):
        slf.tracks = tracks
        slf.carts = carts

    def order_carts(slf):
        slf.carts.sort(key=lambda c: (c.pos.y, c.pos.x))

class Cart:
    def __init__(slf, pos, dir):
        slf.pos = pos
        slf.dir = dir
        slf.turns = 0

    def __repr__(slf):
        return ' '.join(map(str, [slf.pos, slf.dir, slf.turns]))

def parse(data):
    tracks = {}
    carts = []
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            pos = Vec2(x, y)
            if c == '|' or c == '-' or c == '/' or c == '\\' or c == '+':
                tracks[pos] = c
            elif c == '^' or c == 'v':
                tracks[pos] = '|'
                carts.append(Cart(pos, c))
            elif c == '>' or c == '<':
                tracks[pos] = '-'
                carts.append(Cart(pos, c))
    return Madness(tracks, carts)

dir_to_vel = {
    '^' : Vec2(0, -1),
    'v' : Vec2(0, +1),
    '>' : Vec2(+1, 0),
    '<' : Vec2(-1, 0)
}

dir_track_to_dir = {
    ('^', '|') : '^',
    ('^', '\\') : '<',
    ('^', '/') : '>',
    ('v', '|') : 'v',
    ('v', '\\') : '>',
    ('v', '/') : '<',
    ('>', '-') : '>',
    ('>', '\\') : 'v',
    ('>', '/') : '^',
    ('<', '-') : '<',
    ('<', '\\') : '^',
    ('<', '/') : 'v'
}

turn_left = {
    '^' : '<',
    'v' : '>',
    '>' : '^',
    '<' : 'v'
}

turn_right = {
    '^' : '>',
    'v' : '<',
    '>' : 'v',
    '<' : '^'
}

def move_cart(cart, madness):
    # Move the cart.
    cart.pos += dir_to_vel[cart.dir]
    track = madness.tracks[cart.pos]

    # Reorient the cart based on its new track.
    if track == '+':
        if cart.turns == 0:
            cart.dir = turn_left[cart.dir]
        elif cart.turns == 2:
            cart.dir = turn_right[cart.dir]
        cart.turns = (cart.turns + 1) % 3
    else:
        cart.dir = dir_track_to_dir[(cart.dir, track)]


def tick_until_crash(madness):
    while True:
        madness.order_carts()

        # Build a set of occupied positions, for collision checking.
        occupied = set(map(lambda x: x.pos, madness.carts))

        for cart in madness.carts:
            occupied.remove(cart.pos)

            move_cart(cart, madness)

            # Check for collisions.
            if cart.pos in occupied:
                return cart.pos
            else:
                occupied.add(cart.pos)

def tick_until_one_cart(madness):
    while len(madness.carts) > 1:
        madness.order_carts()
        stack = list(reversed(madness.carts))
        while len(stack) > 0:
            cart = stack.pop()
            move_cart(cart, madness)
            for otr in madness.carts:
                if otr != cart and otr.pos == cart.pos:
                    if otr in stack:
                        stack.remove(otr)
                    madness.carts.remove(otr)
                    madness.carts.remove(cart)
    return madness.carts[0].pos

if __name__ == "__main__":
    solve(13, parse, tick_until_crash, tick_until_one_cart)
