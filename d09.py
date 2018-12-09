#!/usr/bin/env python

"""Advent of Code 2018, Day 9"""

import re
import collections

from aoc18 import solve

class MarbleGame:
    def __init__(slf, players, last_marble):
        slf.players = players
        slf.last_marble = last_marble

def parse(data):
    pattern = re.compile("(\d+) players; last marble is worth (\d+) points")
    return MarbleGame(*map(int, re.match(pattern, data).groups()))

def winning_score(game):
    marbles = collections.deque([0])
    score = [0 for _ in range(game.players)]
    for n in range(1, game.last_marble+1):
        if n % 23 == 0:
            player = (n - 1) % game.players
            marbles.rotate(7)
            score[player] += n + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(n)
    return max(score)

def winning_score_100(game):
    return winning_score(MarbleGame(game.players, game.last_marble*100))

if __name__ == "__main__":
    solve(9, parse, winning_score, winning_score_100)
