
#!/usr/bin/env python

"""Advent of Code 2018, Day 25 (Unit Tests)"""

import unittest

from d25 import parse
from d25 import num_constellations

example1=""" 0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0"""

example2="""-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0"""

example3="""1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2"""

example4="""1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2"""

class NumConstellationsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(num_constellations(parse(example1)), 2)

    def test_example2(slf):
        slf.assertEqual(num_constellations(parse(example2)), 4)

    def test_example3(slf):
        slf.assertEqual(num_constellations(parse(example3)), 3)

    def test_example4(slf):
        slf.assertEqual(num_constellations(parse(example4)), 8)

if __name__ == "__main__":
    unittest.main()
