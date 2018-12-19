#!/usr/bin/env python

"""Advent of Code 2018, Day 16"""

import re

from aoc18 import solve
from cpu import ops

class Sample:
    def __init__(slf, before, instr, after):
        slf.before = before
        slf.instr = instr
        slf.after = after

    def __repr__(slf):
        return f'{{B:{slf.before}; I:{slf.instr}, A:{slf.after}}}'

class Input:
    def __init__(slf, samples, program):
        slf.samples = samples
        slf.program = program

def parse(data):
    sections = data.split('\n\n\n\n')

    # Samples
    samples = []
    sample_pattern = re.compile('Before: \[([\d, ]+)\]\n([\d ]+)\nAfter:  \[([\d, ]+)\]')
    for match in re.finditer(sample_pattern, sections[0]):
        groups = match.groups()
        before = [int(x) for x in groups[0].split(', ')]
        instr = [int(x) for x in groups[1].split(' ')]
        after = [int(x) for x in groups[2].split(', ')]
        samples.append(Sample(before, instr, after))

    # Program
    program = [[int(x) for x in line.split(' ')] for line in sections[1].splitlines()]

    return Input(samples, program)

def count_multi_behaviour_samples(input):
    count = 0
    for sample in input.samples:
        valid = 0
        args = sample.instr[1:]
        for op in ops:
            r = list(sample.before)
            op(r, *args)
            valid += int(r == sample.after)
        count += int(valid >= 3)
    return count

def determine_opcodes_and_execute(input):
    possibles = [set(ops) for i in range(16)]
    ops_by_code = [None for i in range(16)]

    # Determine which ops are valid for each opcode.
    for sample in input.samples:
        opcode = sample.instr[0]

        # We've already determined the op for this opcode.
        if ops_by_code[opcode]:
            continue

        # Test out all the possible ops.
        args = sample.instr[1:]
        failed = set()
        possible_ops = possibles[opcode]

        for op in possible_ops:
            r = list(sample.before)
            op(r, *args)
            if r != sample.after:
                failed.add(op)

        # Remove any ops that failed from the list.
        if len(failed) > 0:
            possible_ops -= failed

        # If we have only a single remaining op, then we can resolve the
        # meaning of this opcode, which can cascade to other opcodes.
        if len(possible_ops) == 1:
            resolved = [opcode]
            while len(resolved) > 0:
                opcode = resolved.pop()
                op = next(iter(possibles[opcode]))
                ops_by_code[opcode] = op
                for i, p in enumerate(possibles):
                    if i != opcode and op in p:
                        p.remove(op)
                        if len(p) == 1:
                            resolved.append(i)

    # Run the test program.
    r = [0, 0, 0, 0]
    for instr in input.program:
        ops_by_code[instr[0]](r, *instr[1:])

    return r[0]

if __name__ == "__main__":
    solve(16, parse, count_multi_behaviour_samples, determine_opcodes_and_execute)
