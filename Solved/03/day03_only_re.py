#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 3
def get_year(): return 2024

import re
def parse(ln):
    pattern = r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))'
    return re.findall(pattern, ln)
def p1(v):
    ans = 0
    for m in parse(v):
        if m[0]:
            a, b = map(int, [m[0], m[1]])
            ans += a*b
    return ans

def p2(v):
    ans = 0
    enabled = True
    for m in parse(v):
        if m[0] and enabled:
            a, b = map(int, [m[0], m[1]])
            ans += a*b
        elif m[2]:
            enabled = True
        elif m[3]:
            enabled = False
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
