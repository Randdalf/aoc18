
#!/usr/bin/env python

"""Advent of Code 2018, Day 22 (Unit Tests)"""

import unittest

from d22 import risk_level

class RiskLevelTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(risk_level(510, (10,10)), 114)

if __name__ == "__main__":
    unittest.main()
