
#!/usr/bin/env python

"""Advent of Code 2018, Day 18 (Unit Tests)"""

import unittest

from d18 import parse
from d18 import resource_value

example1=""".#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

class ResourceValueTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(resource_value(parse(example1), 10), 1147)

if __name__ == "__main__":
    unittest.main()
