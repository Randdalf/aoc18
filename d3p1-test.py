#!/usr/bin/env python

"""Advent of Code 2018, Day 3, Puzzle 1 (Unit Tests)"""

import unittest

from d3p1 import solve
from d3 import Rect

class SolveTests(unittest.TestCase):
    def test_example1(slf):
        rects = [
            Rect(1, 1, 3, 4, 4),
            Rect(2, 3, 1, 4, 4),
            Rect(3, 5, 5, 2, 2)
        ]
        slf.assertEqual(solve(rects), 4)

if __name__ == "__main__":
    unittest.main()
