
#!/usr/bin/env python

"""Advent of Code 2018, Day 23 (Unit Tests)"""

import unittest

from d23 import parse
from d23 import in_range_of_largest_radius
from d23 import in_range_of_most_nanobots

example1="""pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""

example2="""pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5"""

class InRangeOfLargestRadiusTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(in_range_of_largest_radius(parse(example1)), 7)

class InRangeOfMostNanobots(unittest.TestCase):
    def test_example2(slf):
        slf.assertEqual(in_range_of_most_nanobots(parse(example2)), 36)

if __name__ == "__main__":
    unittest.main()
