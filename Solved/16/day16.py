#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 16
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

TURNS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def turns(d):
    i = TURNS.index(d)
    return TURNS[(i+1)%4], TURNS[(i-1)%4]

from heapq import heappop as pop, heappush as push
# adj: adj-list where edges are tuples (node_id, weight):
# (1) --2-- (0) --3-- (2) has the adj-list:
# adj = [[(1, 2), (2, 3)], [(0, 2)], [0, 3]]
def dijk(G, S, T):
    INF = 10**18
    dist = defaultdict(lambda: INF)
    pq = []
    def add(node, dst):
        if dst < dist[node]:
            dist[node] = dst
            push(pq, (dst, node))
    add(S, 0)

    while pq:
        D, (P, d) = pop(pq)
        if P == T: return dist, D, d
        if D != dist[P, d]: continue
        a, b = turns(d)
        add((P, a), D + 1000)
        add((P, b), D + 1000)
        nxt = P[0] + d[0], P[1] + d[1]
        if 0 <= nxt[0] < len(G) and 0 <= nxt[1] < len(G[0]):
            if G[nxt[0]][nxt[1]] != '#':
                add((nxt, d), D+1)
    
    return None

def p1(v):
    G = get_lines(v)
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == 'S':
                S = i, j
            if G[i][j] == 'E':
                E = i, j
    dst1, tot, dir = dijk(G, (S, (0, 1)), E)
    return tot


def p2(v):
    G = get_lines(v)
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == 'S':
                S = i, j
            if G[i][j] == 'E':
                E = i, j
    dst1, tot, dir = dijk(G, (S, (0, 1)), E)
    dir2 = TURNS[TURNS.index(dir) - 2]
    dst2, tot2, _ =  dijk(G, (E, dir2), S)
    ans = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            ok = False
            for k in range(4):
                dst = dst1[(i, j), TURNS[k]] + dst2[(i, j), TURNS[k-2]]
                if dst == tot:
                    ok = True
            if ok:
                ans += 1
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
