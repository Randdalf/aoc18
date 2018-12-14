
#!/usr/bin/env python

"""Advent of Code 2018, Day 14 (Unit Tests)"""

import unittest

from d14 import ten_scores_after_num
from d14 import recipes_before_num

class TenScoresAfterNumTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(ten_scores_after_num(9), "5158916779")

    def test_example2(slf):
        slf.assertEqual(ten_scores_after_num(5), "0124515891")

    def test_example3(slf):
        slf.assertEqual(ten_scores_after_num(18), "9251071085")

    def test_example4(slf):
        slf.assertEqual(ten_scores_after_num(2018), "5941429882")

class RecipesBeforeNumTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(recipes_before_num(51589), 9)

    def test_example2(slf):
        slf.assertEqual(recipes_before_num(1245), 6)

    def test_example3(slf):
        slf.assertEqual(recipes_before_num(92510), 18)

    def test_example4(slf):
        slf.assertEqual(recipes_before_num(59414), 2018)

if __name__ == "__main__":
    unittest.main()
