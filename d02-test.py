#!/usr/bin/env python

"""Advent of Code 2018, Day 2 (Unit Tests)"""

import unittest
import itertools

from d02 import checksum_ids
from d02 import intersect_closest_ids

class ChecksumIdsTests(unittest.TestCase):
    def test_example1(slf):
        ids = [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab'
        ]
        slf.assertEqual(checksum_ids(ids), 12)

    def test_example2(slf):
        ids = [
            'aax',
            'bbb',
            'ccx',
            'ccc'
        ]
        slf.assertEqual(checksum_ids(ids), 4)

class IntersectClosestIdsTests(unittest.TestCase):
    def test_example1(slf):
        ids = [
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz'
        ]
        slf.assertEqual(intersect_closest_ids(ids), 'fgij')

if __name__ == "__main__":
    unittest.main()
