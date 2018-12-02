#!/usr/bin/env python

"""Advent of Code 2018, Day 2, Puzzle 1 (Unit Tests)"""

import unittest

from d2p1 import solve

class SolveTests(unittest.TestCase):
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
        slf.assertEqual(solve(ids), 12)

    def test_example2(slf):
        ids = [
            'aax',
            'bbb',
            'ccx',
            'ccc'
        ]
        slf.assertEqual(solve(ids), 4)

if __name__ == "__main__":
    unittest.main()
