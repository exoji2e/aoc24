#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 12
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def perimiter(q):
    S = set(q)
    ans = 0
    for x, y in q:
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (nx, ny) not in S:
                ans += 1
    return ans

def sides(q):
    S = set(q)
    ans = 0
    perim = set()
    for x, y in q:
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (nx, ny) not in S:
                perim.add((nx, ny, x, y))
    for x, y, ox, oy in perim:
        if (x-1, y, ox-1, oy) in perim: continue
        if (x, y-1, ox, oy-1) in perim: continue

        ans += 1
    return ans

def p1(v):
    G = get_lines(v)
    R, C = len(G), len(G[0])
    ans = 0
    seen = set()
    for r in range(R):
        for c in range(C):
            if (r, c) in seen: continue
            seen.add((r, c))
            q = [(r, c)]
            for x, y in q:
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < R and 0 <= ny < C and G[nx][ny] == G[r][c]:
                        if (nx, ny) not in seen:
                            q.append((nx, ny))
                            seen.add((nx, ny))
            area = len(q)
            P = perimiter(q)
            ans += area * P
    return ans

def p2(v):
    G = get_lines(v)
    R, C = len(G), len(G[0])
    ans = 0
    seen = set()
    for r in range(R):
        for c in range(C):
            if (r, c) in seen: continue
            seen.add((r, c))
            q = [(r, c)]
            for x, y in q:
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < R and 0 <= ny < C and G[nx][ny] == G[r][c]:
                        if (nx, ny) not in seen:
                            q.append((nx, ny))
                            seen.add((nx, ny))
            area = len(q)
            S = sides(q)
            ans += area * S
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
