#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 6
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

NDIR = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

def getPath(G, pos, dir, extra):
    seen = set()
    def get(r, c):
        if (r, c) == extra: return '#'
        if 0 <= r < len(G) and 0 <= c < len(G[0]):
            return G[r][c]
        return '-'
    while True:
        if (pos, dir) in seen: return True, seen
        seen.add((pos, dir))
        r, c = pos
        nr, nc = r+dir[0], c+dir[1]
        if get(nr,nc) == '-': return False, seen
        if get(nr,nc) == '#':
            dir = NDIR[dir]
            continue
        pos = nr, nc
    

def p1(v):
    save_input(v)
    G = [list(l) for l in get_lines(v)]
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] == '^':
                pos = r, c
    dir = -1, 0
    _, seen = getPath(G, pos, dir, None)
    return len({p for p, _ in seen})
# 1792
def p2(v):
    G = [list(l) for l in get_lines(v)]
    for r in range(len(G)):
        for c in range(len(G[0])):
            if G[r][c] == '^':
                pos = r, c
    dir = -1, 0
    ans = 0
    _, seen = getPath(G, pos, dir, None)
    for blocked in {p for p, _ in seen}:
        loop, _ = getPath(G, pos, dir, blocked)
        if loop: ans += 1
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
