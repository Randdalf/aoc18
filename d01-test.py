#!/usr/bin/env python

"""Advent of Code 2018, Day 1 (Unit Tests)"""

import unittest
import itertools

from d01 import sum_deltas
from d01 import find_repeated_freq

class SumDeltaTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(sum_deltas([+1, -2, +3, +1]), 3)

    def test_example2(slf):
        slf.assertEqual(sum_deltas([+1, +1, +1]), 3)

    def test_example3(slf):
        slf.assertEqual(sum_deltas([+1, +1, -2]), 0)

    def test_example4(slf):
        slf.assertEqual(sum_deltas([-1, -2, -3]), -6);

    def test_generator_range(slf):
        slf.assertEqual(sum_deltas(range(0, 5)), 10)

    def test_generator_repeat(slf):
        slf.assertEqual(sum_deltas(itertools.repeat(3, 17)), 3 * 17)

class FindRepeatedFreqTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(find_repeated_freq([+1, -2, +3, +1, +1, -2]), 2)

    def test_example2(slf):
        slf.assertEqual(find_repeated_freq([+1, -1]), 0)

    def test_example3(slf):
        slf.assertEqual(find_repeated_freq([+3, +3, +4, -2, -4]), 10)

    def test_example4(slf):
        slf.assertEqual(find_repeated_freq([-6, +3, +8, +5, -6]), 5)

    def test_example5(slf):
        slf.assertEqual(find_repeated_freq([+7, +7, -2, -7, -4]), 14)

if __name__ == "__main__":
    unittest.main()
