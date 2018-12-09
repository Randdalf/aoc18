
#!/usr/bin/env python

"""Advent of Code 2018, Day 9 (Unit Tests)"""

import unittest

from d09 import MarbleGame
from d09 import winning_score

example1 = MarbleGame(9, 32)
example2 = MarbleGame(10, 1618)
example3 = MarbleGame(13, 7999)
example4 = MarbleGame(17, 1104)
example5 = MarbleGame(21, 6111)
example6 = MarbleGame(30, 5807)

class WinningScoreTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(winning_score(example1), 32)

    def test_example2(slf):
        return slf.assertEqual(winning_score(example2), 8317)

    def test_example3(slf):
        return slf.assertEqual(winning_score(example3), 146373)

    def test_example4(slf):
        return slf.assertEqual(winning_score(example4), 2764)

    def test_example5(slf):
        return slf.assertEqual(winning_score(example5), 54718)

    def test_example6(slf):
        return slf.assertEqual(winning_score(example6), 37305)

if __name__ == "__main__":
    unittest.main()
