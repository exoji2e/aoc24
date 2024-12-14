#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 14
def get_year(): return 2024

def parse(ln):
    x, y, vx, vy = lazy_ints(multi_split(ln, ' p=,v'))
    return (x, y), (vx, vy)

H = 103
W = 101
def walk(p, v):
    curr = p
    for _ in range(100):
        curr = (curr[0] + v[0])%W, (curr[1] + v[1])%H
    return curr

def step(Pts):
    pts2 = []
    for p, v in Pts:
        nxt = (p[0] + v[0])%W, (p[1] + v[1])%H
        pts2.append((nxt, v))
    return pts2

def cluster(Pts):
    cnt = 0
    ps = Counter()
    for p, _ in Pts:
        ps[p] += 1
    for p, c in ps.items():
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                neigh = (p[0] + dx, p[1] + dy)
                if neigh != p:
                    cnt += c*ps[neigh]
    return cnt

def p1(v):
    lns = get_lines(v)
    quadrants = [0]*4
    global H, W
    S = [[0]*W for _ in range(H)]
    G = [[0]*W for _ in range(H)]
    for ln in lns:
        p, v = parse(ln)
        last = walk(p, v)
        S[p[1]][p[0]] += 1
        G[last[1]][last[0]] += 1
        if last[0] < W//2 and last[1] < H//2:
            quadrants[0] += 1
        if last[0] < W//2 and last[1] > H//2:
            quadrants[1] += 1
        if last[0] > W//2 and last[1] < H//2:
            quadrants[2] += 1
        if last[0] > W//2 and last[1] > H//2:
            quadrants[3] += 1
    Q = quadrants
    return Q[0]*Q[1]*Q[2]*Q[3]

def p2(v):
    lns = get_lines(v)
    global H, W
    Pts = []
    for ln in lns:
        p, v = parse(ln)
        Pts.append((p, v))
    for i in range(1, 100000):
        Pts = step(Pts)
        cnt = cluster(Pts)
        if cnt > 1000:
            S = [[0]*W for _ in range(H)]
            for p, _ in Pts:
                S[p[1]][p[0]] += 1
            # print('\n'.join([''.join(['#' if x else ' ' for x in row]) for row in S]))
            return i

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
