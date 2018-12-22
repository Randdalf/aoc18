
#!/usr/bin/env python

"""Advent of Code 2018, Day 22 (Unit Tests)"""

import unittest

from d22 import Cave
from d22 import risk_level
from d22 import shortest_path

class RiskLevelTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(risk_level(Cave(510, (10,10))), 114)

class ShortestPathTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(shortest_path(Cave(510, (10,10))), 45)

if __name__ == "__main__":
    unittest.main()
