#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid
def get_day(): return 18
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ','))

SZ = 70
def p1(v):
    lns = get_lines(v)
    G = Grid.fromSize(SZ+1, SZ+1, '.')
    for ln in lns[:1024]:
        x, y = parse(ln)
        G[y, x] = '#'
    return G.bfs((0, 0), T=(SZ, SZ))

def p2(v):
    lns = get_lines(v)
    G = Grid.fromSize(SZ+1, SZ+1, '.')
    for ln in lns:
        x, y = parse(ln)
        G[y,x] = '#'
        if G.bfs((0, 0), T=(SZ, SZ)) == -1:
            return ln

if __name__ == '__main__':
    options = get_commands()
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
