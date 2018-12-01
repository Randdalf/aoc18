#!/usr/bin/env python

"""Advent of Code 2018, Day 1, Puzzle 2 (Unit Tests)"""

import unittest

from d1p2 import solve

class SolveTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(solve([+1, -2, +3, +1, +1, -2]), 2)

    def test_example2(slf):
        slf.assertEqual(solve([+1, -1]), 0)

    def test_example3(slf):
        slf.assertEqual(solve([+3, +3, +4, -2, -4]), 10)

    def test_example4(slf):
        slf.assertEqual(solve([-6, +3, +8, +5, -6]), 5)

    def test_example5(slf):
        slf.assertEqual(solve([+7, +7, -2, -7, -4]), 14)

if __name__ == "__main__":
    unittest.main()
