#!/usr/bin/env python

"""Advent of Code 2018, Day 3 (Unit Tests)"""

import unittest

from d03 import Rect
from d03 import count_occupied_squares

class FindSleepiestGuard2Tests(unittest.TestCase):
    def test_example1(slf):
        rects = [
            Rect(1, 1, 3, 4, 4),
            Rect(2, 3, 1, 4, 4),
            Rect(3, 5, 5, 2, 2)
        ]
        slf.assertEqual(count_occupied_squares(rects), 4)

if __name__ == "__main__":
    unittest.main()
