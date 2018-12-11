
#!/usr/bin/env python

"""Advent of Code 2018, Day 11 (Unit Tests)"""

import unittest

from d11 import power_level
from d11 import largest_total_power

class PowerLevelTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(power_level(3, 5, 8), 4)

    def test_example2(slf):
        slf.assertEqual(power_level(122, 79, 57), -5)

    def test_example3(slf):
        slf.assertEqual(power_level(217, 196, 39), 0)

    def test_example4(slf):
        slf.assertEqual(power_level(101, 153, 71), 4)

class LargestTotalPower(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(largest_total_power(18, 3, 3), (33, 45, 3))

    def test_example2(slf):
        slf.assertEqual(largest_total_power(42, 3, 3), (21, 61, 3))

    def test_example3(slf):
        slf.assertEqual(largest_total_power(18, 1, 300), (90, 269, 16))

    def test_example4(slf):
        slf.assertEqual(largest_total_power(42, 1, 300), (232, 251, 12))

if __name__ == "__main__":
    unittest.main()
