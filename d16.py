#!/usr/bin/env python

"""Advent of Code 2018, Day 16"""

import re

from aoc18 import solve

class Sample:
    def __init__(slf, before, instr, after):
        slf.before = before
        slf.instr = instr
        slf.after = after

    def __repr__(slf):
        return f'{{B:{slf.before}; I:{slf.instr}, A:{slf.after}}}'

class Input:
    def __init__(slf, samples):
        slf.samples = samples

class RegisterError(Exception):
    pass

def store(r, i, v):
    if i < 0 or i > 3:
        raise RegisterError()
    r[i] = v

def get(r, i):
    if i < 0 or i > 3:
        raise RegisterError()
    return r[i]

def addr(r, a, b, c):
    """(add register) stores into register C the result of adding register A and register B."""
    store(r, c, get(r, a) + get(r, b))

def addi(r, a, b, c):
    """(add immediate) stores into register C the result of adding register A and value B."""
    store(r, c, get(r, a) + b)

def mulr(r, a, b, c):
    """(multiply register) stores into register C the result of multiplying register A and register B."""
    store(r, c, get(r, a) * get(r, b))

def muli(r, a, b, c):
    """(multiply immediate) stores into register C the result of multiplying register A and value B."""
    store(r, c, get(r, a) * b)

def banr(r, a, b, c):
    """(bitwise AND register) stores into register C the result of the bitwise AND of register A and register B."""
    store(r, c, get(r, a) & get(r, b))

def bani(r, a, b, c):
    """bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B."""
    store(r, c, get(r, a) & b)

def borr(r, a, b, c):
    """(bitwise OR register) stores into register C the result of the bitwise OR of register A and register B."""
    store(r, c, get(r, a) | get(r, b))

def bori(r, a, b, c):
    """(bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B."""
    store(r, c, get(r, a) | b)

def setr(r, a, b, c):
    """(set register) copies the contents of register A into register C. (Input B is ignored.)"""
    store(r, c, get(r, a))

def seti(r, a, b, c):
    """(set immediate) stores value A into register C. (Input B is ignored.)"""
    store(r, c, a)

def gtir(r, a, b, c):
    """(greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0."""
    store(r, c, int(a > get(r, b)))

def gtri(r, a, b, c):
    """(greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0."""
    store(r, c, int(get(r, a) > b))

def gtrr(r, a, b, c):
    """(greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0."""
    store(r, c, int(get(r, a) > get(r, b)))

def eqir(r, a, b, c):
    """(equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0."""
    store(r, c, int(a == get(r, b)))

def eqri(r, a, b, c):
    """(equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0."""
    store(r, c, int(get(r, a) == b))

def eqrr(r, a, b, c):
    """(equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0."""
    store(r, c, int(get(r, a) == get(r, b)))

ops = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr
]

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

    return Input(samples)

def count_multi_behaviour_samples(input):
    count = 0
    for sample in input.samples:
        valid = 0
        args = sample.instr[1:]
        for op in ops:
            r = list(sample.before)
            try:
                op(r, *args)
                valid += int(r == sample.after)
            except RegisterError:
                pass
        count += int(valid >= 3)
    return count

if __name__ == "__main__":
    solve(16, parse, count_multi_behaviour_samples)
