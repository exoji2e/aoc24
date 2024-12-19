#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 19
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def possible(ln, patterns):
    seen = Counter()
    seen[0] = 1
    for u in range(len(ln)):
        if seen[u] == 0:
            continue
        cnt = seen[u]
        for pat in patterns:
            if ln[u:u+len(pat)] == pat:
                v = u + len(pat)
                seen[v] += cnt
    return seen[len(ln)]
def p1(v):
    chunks = v.split('\n\n')
    patterns = chunks[0].split(', ')
    ans = 0
    for ln in chunks[1].split('\n'):
        if possible(ln, patterns):
            ans += 1
    return ans

def p2(v):
    chunks = v.split('\n\n')
    patterns = chunks[0].split(', ')
    ans = 0
    for ln in chunks[1].split('\n'):
        v = possible(ln, patterns)
        ans += v
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
