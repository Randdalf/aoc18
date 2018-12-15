
#!/usr/bin/env python

"""Advent of Code 2018, Day 15 (Unit Tests)"""

import unittest

from d15 import parse
from d15 import outcome

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

class OutcomeTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(outcome(parse(example1)), 27730)

    def test_example2(slf):
        slf.assertEqual(outcome(parse(example2)), 36334)

    def test_example3(slf):
        slf.assertEqual(outcome(parse(example3)), 39514)

    def test_example4(slf):
        slf.assertEqual(outcome(parse(example4)), 27755)

    def test_example5(slf):
        slf.assertEqual(outcome(parse(example5)), 28944)

    def test_example6(slf):
        slf.assertEqual(outcome(parse(example6)), 18740)

if __name__ == "__main__":
    unittest.main()
