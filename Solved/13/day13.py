#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 13
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

import z3
def play2(lines):
    xA, yA = lazy_ints(multi_split(lines[0].split(':')[1], ' =XY+,'))
    xB, yB = lazy_ints(multi_split(lines[1].split(':')[1], ' =XY+,'))
    xP, yP = lazy_ints(multi_split(lines[2].split(':')[1], ' =XY+,'))
    xP += 10000000000000
    yP += 10000000000000
    s = z3.Solver()
    a = z3.Int('a')
    b = z3.Int('b')
    s.add(xA*a + xB*b == xP)
    s.add(yA*a + yB*b == yP)
    res = s.check()
    if res == z3.sat:
        model= s.model()
        vs = [model.evaluate(var).as_long() for var in [a, b]]
        return 3*vs[0] + vs[1]
    return 0

def play(lines):
    xA, yA = lazy_ints(multi_split(lines[0].split(':')[1], ' =XY+,'))
    xB, yB = lazy_ints(multi_split(lines[1].split(':')[1], ' =XY+,'))
    xP, yP = lazy_ints(multi_split(lines[2].split(':')[1], ' =XY+,'))
    low_cost = 10**9
    for a in range(101):
        for b in range(101):
            if 3*a + b < low_cost:
                if xA*a + xB*b == xP and yA*a + yB*b == yP:
                    low_cost = 3*a + b
    if low_cost == 10**9:
        return 0
    return low_cost

def p1(v):
    chunks = v.split('\n\n')
    ans = 0
    for chunk in chunks:
        ans += play(chunk.split('\n'))
    return ans

def p2(v):
    chunks = v.split('\n\n')
    ans = 0
    for chunk in chunks:
        ans += play2(chunk.split('\n'))
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
