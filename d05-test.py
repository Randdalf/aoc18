
#!/usr/bin/env python

"""Advent of Code 2018, Day 5 (Unit Tests)"""

import unittest

from d05 import len_react
from d05 import improve

class LenReactTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(len_react('aA'), 0)

    def test_example2(slf):
        slf.assertEqual(len_react('abBA'), 0)

    def test_example3(slf):
        slf.assertEqual(len_react('abAB'), 4)

    def test_example4(slf):
        slf.assertEqual(len_react('aabAAB'), 6)

    def test_example5(slf):
        slf.assertEqual(len_react('dabAcCaCBAcCcaDA'), 10)

class ImproveTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(improve('dabAcCaCBAcCcaDA'), 4)

if __name__ == "__main__":
    unittest.main()
