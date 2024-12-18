#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 18
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ','))
sz = 70
def path(G):
    q = [(0, 0)]
    seen = set(q)
    no = 0
    while q:
        q2 = []
        for x, y in q:
            if (x, y) == (sz, sz):
                return no
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx <= sz and 0 <= ny <= sz and (nx, ny) not in seen and G[ny][nx] == '.':
                    q2.append((nx, ny))
                    seen.add((nx, ny))
        q = q2
        no += 1
    return -1

def p1(v):
    lns = get_lines(v)
    G = [['.' for _ in range(sz + 1)] for _ in range(sz + 1)]
    for ln in lns[:1024]:
        x, y = parse(ln)
        G[y][x] = '#'
    return path(G)

def p2(v):
    lns = get_lines(v)
    G = [['.' for _ in range(sz + 1)] for _ in range(sz + 1)]
    for ln in lns:
        x, y = parse(ln)
        G[y][x] = '#'
        if path(G) == -1:
            return ln

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
