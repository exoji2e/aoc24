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
    return re.finditer(r'mul\((\d+),(\d+)\)', ln)
def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        for m in parse(ln):
            a, b = map(int, [m.group(1), m.group(2)])
            ans += a*b
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    enabled = True
    for ln in lns:
        OK = []
        for i in range(len(ln)):
            if ln[i:i+4] == 'do()':
                enabled = True
            elif ln[i:i+7] == 'don\'t()':
                enabled = False
            OK.append(enabled)
        for m in parse(ln):
            if OK[m.start()]:
                a, b = map(int, [m.group(1), m.group(2)])
                ans += a*b
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
