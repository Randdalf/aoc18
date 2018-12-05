
#!/usr/bin/env python

"""Advent of Code 2018, Day 5 (Unit Tests)"""

import unittest

from d05 import react

class ReactTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(react('aA'), 0)

    def test_example2(slf):
        slf.assertEqual(react('abBA'), 0)

    def test_example3(slf):
        slf.assertEqual(react('abAB'), 4)

    def test_example4(slf):
        slf.assertEqual(react('aabAAB'), 6)

    def test_example5(slf):
        slf.assertEqual(react('dabAcCaCBAcCcaDA'), 10)

if __name__ == "__main__":
    unittest.main()
