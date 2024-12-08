#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 8
def get_year(): return 2024

def parse(v):
    G = get_lines(v)
    positions = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] != '.':
                positions.append((i, j, G[i][j]))
    return positions, G

def p1(v):
    positions, G = parse(v)
    P = set()
    for a, b, v in positions:
        for c, d, v2 in positions:
            if v != v2: continue
            if a == c and b == d: continue
            dx = c - a
            dy = d - b
            px = c + dx
            py = d + dy
            if 0 <= px < len(G) and 0 <= py < len(G[0]):
                P.add((px, py))
    return len(P)

def p2(v):
    positions, G = parse(v)
    P = set()
    for a, b, v in positions:
        for c, d, v2 in positions:
            if v != v2: continue
            if a == c and b == d: continue
            dx = c - a
            dy = d - b
            for i in range(0, 1000):
                px = c + i*dx
                py = d + i*dy
                if 0 <= px < len(G) and 0 <= py < len(G[0]):
                    P.add((px, py))
                else: break
    return len(P)

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
