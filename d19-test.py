
#!/usr/bin/env python

"""Advent of Code 2018, Day 19 (Unit Tests)"""

import unittest

from d19 import parse
from d19 import execute

example1="""#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5"""

class ExecuteTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(execute(parse(example1)), 6)

if __name__ == "__main__":
    unittest.main()
