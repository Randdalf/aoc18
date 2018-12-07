
#!/usr/bin/env python

"""Advent of Code 2018, Day 7 (Unit Tests)"""

import unittest

from d07 import determine_order

class DetermineOrderTests(unittest.TestCase):
    def test_example1(slf):
        instructions = [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E')
        ]
        slf.assertEqual(determine_order(instructions), "CABDFE")

if __name__ == "__main__":
    unittest.main()
