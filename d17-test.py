
#!/usr/bin/env python

"""Advent of Code 2018, Day 17 (Unit Tests)"""

import unittest

from d17 import parse
from d17 import count_all_water

example1="""x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504"""

class CountWaterTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(count_all_water(parse(example1)), 57)

if __name__ == "__main__":
    unittest.main()
