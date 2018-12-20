
#!/usr/bin/env python

"""Advent of Code 2018, Day 20 (Unit Tests)"""

import unittest

from d20 import most_doors_to_room

class MostDoorsToRoomTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(most_doors_to_room("WNE"), 3)

    def test_example2(slf):
        slf.assertEqual(most_doors_to_room("ENWWW(NEEE|SSE(EE|N))"), 10)

    def test_example3(slf):
        slf.assertEqual(most_doors_to_room("ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN"), 18)

    def test_example4(slf):
        slf.assertEqual(most_doors_to_room("ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))"), 23)

    def test_example5(slf):
        slf.assertEqual(most_doors_to_room("WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))"), 31)

if __name__ == "__main__":
    unittest.main()
