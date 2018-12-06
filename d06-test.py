
#!/usr/bin/env python

"""Advent of Code 2018, Day 6 (Unit Tests)"""

import unittest

from d06 import Coord
from d06 import largest_finite_area

class LargestFiniteAreaTests(unittest.TestCase):
    def test_example1(slf):
        coords = [
            Coord(1, 1),
            Coord(1, 6),
            Coord(8, 3),
            Coord(3, 4),
            Coord(5, 5),
            Coord(8, 9)
        ]
        slf.assertEqual(largest_finite_area(coords), 17)

if __name__ == "__main__":
    unittest.main()
