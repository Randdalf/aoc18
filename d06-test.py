
#!/usr/bin/env python

"""Advent of Code 2018, Day 6 (Unit Tests)"""

import unittest

from d06 import Coord
from d06 import largest_finite_area
from d06 import area_within_total_dist

example1 = [
    Coord(1, 1),
    Coord(1, 6),
    Coord(8, 3),
    Coord(3, 4),
    Coord(5, 5),
    Coord(8, 9)
]

class LargestFiniteAreaTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(largest_finite_area(example1), 17)

class AreaWithTotalDistTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(area_within_total_dist(example1, 32), 16)

if __name__ == "__main__":
    unittest.main()
