#!/usr/bin/env python

"""Advent of Code 2018, Day 9"""

import re

from aoc18 import solve

class MarbleGame:
    def __init__(slf, players, last_marble):
        slf.players = players
        slf.last_marble = last_marble

class Marble:
    def __init__(slf, n, prev, next):
        slf.n = n
        slf.prev = prev
        slf.next = next

def parse(data):
    pattern = re.compile("(\d+) players; last marble is worth (\d+) points")
    return MarbleGame(*map(int, re.match(pattern, data).groups()))

def winning_score(game):
    current_marble = Marble(0, None, None)
    current_marble.prev = current_marble
    current_marble.next = current_marble
    score = [0 for _ in range(game.players)]
    for n in range(1, game.last_marble+1):
        if n % 23 == 0:
            player = (n - 1) % game.players
            anti_clockwise_7 = current_marble
            for _ in range(7):
                anti_clockwise_7 = anti_clockwise_7.prev
            anti_clockwise_7.prev.next = anti_clockwise_7.next
            anti_clockwise_7.next.prev = anti_clockwise_7.prev
            current_marble = anti_clockwise_7.next
            score[player] += n + anti_clockwise_7.n
        else:
            clockwise_1 = current_marble.next
            clockwise_2 = clockwise_1.next
            current_marble = Marble(n, clockwise_1, clockwise_2)
            clockwise_1.next = current_marble
            clockwise_2.prev = current_marble
    return max(score)

def winning_score_100(game):
    return winning_score(MarbleGame(game.players, game.last_marble*100))

if __name__ == "__main__":
    solve(9, parse, winning_score, winning_score_100)
