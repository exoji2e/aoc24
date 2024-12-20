#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 20
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))
from grid import Grid

def p1(v):
    lns = get_lines(v)
    G = Grid(lns)
    S = next(G.findAll('S'))
    E = next(G.findAll('E'))
    time = G.bfs(S, T=E)
    cnt = 0
    for i, (r, c) in enumerate(G.coords()):
        if G[r, c] == '#':
            G[r,c] = '.'
            t2 = G.bfs(S, T=E)
            if t2 + 100 <= time:
                cnt += 1
            G[r,c] = '#'
    return cnt

def p2(v):
    lns = get_lines(v)
    G = Grid(lns)
    S = next(G.findAll('S'))
    E = next(G.findAll('E'))
    D = G.bfs(S)
    D2 = G.bfs(E)
    tot = D[E]
    ans = 0
    C = Counter()
    for p in G.coords():
        for dx in range(-20, 21):
            for dy in range(-20, 21):
                dst = abs(dx) + abs(dy)
                if dst > 20: continue
                if dx == 0 and dy == 0: continue
                p2 = p + (dx, dy)
                cheat = D[p] + D2[p2] + dst
                
                if cheat + 100 <= tot:
                    ans += 1
                    saved = tot - cheat
                    C[saved] += 1
    # print(*sorted(C.items()), sep='\n')
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
