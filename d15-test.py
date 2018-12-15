
#!/usr/bin/env python

"""Advent of Code 2018, Day 15 (Unit Tests)"""

import unittest

from d15 import parse
from d15 import default_outcome
from d15 import elves_win_outcome

example1="""#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""

example2="""#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

example3="""#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

example4="""#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""

example5="""#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""

example6="""#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""

class DefaultOutcomeTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(default_outcome(parse(example1)), 27730)

    def test_example2(slf):
        slf.assertEqual(default_outcome(parse(example2)), 36334)

    def test_example3(slf):
        slf.assertEqual(default_outcome(parse(example3)), 39514)

    def test_example4(slf):
        slf.assertEqual(default_outcome(parse(example4)), 27755)

    def test_example5(slf):
        slf.assertEqual(default_outcome(parse(example5)), 28944)

    def test_example6(slf):
        slf.assertEqual(default_outcome(parse(example6)), 18740)

class ElvesWinOutcome(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(elves_win_outcome(parse(example1)), 4988)

    def test_example3(slf):
        slf.assertEqual(elves_win_outcome(parse(example3)), 31284)

    def test_example4(slf):
        slf.assertEqual(elves_win_outcome(parse(example4)), 3478)

    def test_example5(slf):
        slf.assertEqual(elves_win_outcome(parse(example5)), 6474)

    def test_example6(slf):
        slf.assertEqual(elves_win_outcome(parse(example6)), 1140)

if __name__ == "__main__":
    unittest.main()
