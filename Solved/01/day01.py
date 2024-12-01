#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 1
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    lns = get_lines(v)
    ans = 0
    l, r = [], []
    for ln in lns:
        a, b = parse(ln)
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    for a, b in zip(l, r):
        ans += abs(a - b)
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    l, r = [], []
    for ln in lns:
        a, b = parse(ln)
        l.append(a)
        r.append(b)
    C = Counter(r)
    for a in l:
        ans += a*C[a]
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
