#!/usr/bin/env python

"""Advent of Code 2018, Day 1, Puzzle 1 (Unit Tests)"""

import unittest
import itertools

from d1p1 import solve

class SolveTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(solve([+1, -2, +3, +1]), 3)

    def test_example2(slf):
        slf.assertEqual(solve([+1, +1, +1]), 3)

    def test_example3(slf):
        slf.assertEqual(solve([+1, +1, -2]), 0)

    def test_example4(slf):
        slf.assertEqual(solve([-1, -2, -3]), -6);

    def test_generator_range(slf):
        slf.assertEqual(solve(range(0, 5)), 10)

    def test_generator_repeat(slf):
        slf.assertEqual(solve(itertools.repeat(3, 17)), 3 * 17)

if __name__ == "__main__":
    unittest.main()
