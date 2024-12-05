#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 5
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def sort(ints, order):
    ch = False
    for i in range(len(ints)):
        for j in range(i+1, len(ints)):
            if (ints[j], ints[i]) in order:
                ints[i], ints[j] = ints[j], ints[i]
                ch = True
    return ch

def p1(v):
    chunks = v.split('\n\n')
    order = {tuple(lazy_ints(ln.split('|'))) for ln in get_lines(chunks[0])}
    lns = get_lines(chunks[1])
    ans = 0
    for ln in lns:
        ints = lazy_ints(ln.split(','))
        if not sort(ints, order):
            ans += ints[len(ints)//2]
    return ans

def p2(v):
    chunks = v.split('\n\n')
    order = {tuple(lazy_ints(ln.split('|'))) for ln in get_lines(chunks[0])}
    lns = get_lines(chunks[1])
    ans = 0
    for ln in lns:
        ints = lazy_ints(ln.split(','))
        if sort(ints, order):
            ans += ints[len(ints)//2]
    return ans

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
