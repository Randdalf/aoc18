
#!/usr/bin/env python

"""Advent of Code 2018, Day 7 (Unit Tests)"""

import unittest

from d07 import work_order
from d07 import work_time

example1 = [
    ('C', 'A'),
    ('C', 'F'),
    ('A', 'B'),
    ('A', 'D'),
    ('B', 'E'),
    ('D', 'E'),
    ('F', 'E')
]

class WorkOrderTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(work_order(example1), "CABDFE")

class WorkTimeTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(work_time(example1, 0, 2), 15)

if __name__ == "__main__":
    unittest.main()
