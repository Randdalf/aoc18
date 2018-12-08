
#!/usr/bin/env python

"""Advent of Code 2018, Day 8 (Unit Tests)"""

import unittest

from d08 import parse
from d08 import sum_metadata

example1 = parse("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")

class SumMetadataTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(sum_metadata(example1), 138)

if __name__ == "__main__":
    unittest.main()
