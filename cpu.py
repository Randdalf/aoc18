#!/usr/bin/env python

"""Advent of Code 2018, CPU Instructions"""

def store(r, i, v):
    """Store value v in register i."""
    r[i] = v

def get(r, i):
    """Retrieve value in register i."""
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


class Program:
    def __init__(slf, ipr, instrs):
        slf.ipr = ipr
        slf.instrs = instrs

def parse(data):
    lines = data.splitlines()
    ipr = int(lines[0].split(' ')[1])
    ops_by_name = {op.__name__: op for op in ops}
    instrs = []
    for line in lines[1:]:
        parts = line.split(' ')
        instrs.append((ops_by_name[parts[0]], tuple(map(int, parts[1:]))))
    return Program(ipr, instrs)

def execute(program, r, max_cycles, ip=0, verbose=False):
    ipr = program.ipr
    instrs = program.instrs
    cycles = 0
    while 0 <= ip < len(instrs) and cycles < max_cycles:
        r[ipr] = ip
        instr = instrs[ip]
        instr[0](r, *instr[1])
        if verbose:
            print(instr[0].__name__, instr[1], '=>', r)
        ip = r[ipr] + 1
        cycles += 1
    return ip
