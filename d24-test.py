
#!/usr/bin/env python

"""Advent of Code 2018, Day 24 (Unit Tests)"""

import unittest

from d24 import parse
from d24 import simulate

example1="""Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

class SimulateTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(simulate(parse(example1), verbose=True), 5216)

if __name__ == "__main__":
    unittest.main()
