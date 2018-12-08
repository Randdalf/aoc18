#!/usr/bin/env python

"""Advent of Code 2018, Day 8"""

from aoc18 import solve

class TreeNode:
    def __init__(slf, data):
        child_count = next(data)
        meta_count = next(data)
        slf.children = [TreeNode(data) for _ in range(child_count)]
        slf.metadata = [next(data) for _ in range(meta_count)]

def parse(data):
    return TreeNode(map(int, data.split(' ')))

def sum_metadata(node):
    return sum(node.metadata) + sum(map(sum_metadata, node.children))

def node_value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
    else:
        return sum(map(lambda i: node_value(node.children[i-1]), filter(lambda i: 1 <= i <= len(node.children), node.metadata)))

if __name__ == "__main__":
    solve(8, parse, sum_metadata, node_value)
