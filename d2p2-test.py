#!/usr/bin/env python

"""Advent of Code 2018, Day 2, Puzzle 2 (Unit Tests)"""

import unittest

from d2p2 import solve

class SolveTests(unittest.TestCase):
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
        slf.assertEqual(solve(ids), 'fgij')

if __name__ == "__main__":
    unittest.main()
