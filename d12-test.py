
#!/usr/bin/env python

"""Advent of Code 2018, Day 12 (Unit Tests)"""

import unittest

from d12 import parse
from d12 import sum_after_20_gens

example1="""initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

class SumAfter20GensTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(sum_after_20_gens(parse(example1)), 325)

if __name__ == "__main__":
    unittest.main()
