#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 10
def get_year(): return 2024

def walk1(x, y, G):
    q = [(x, y)]
    seen = set(q)
    ans = 0
    for x, y in q:
        if G[x][y] == 9:
            ans += 1
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < len(G) and 0 <= ny < len(G[0]) and G[nx][ny] == 1 + G[x][y]:
                if (nx, ny) not in seen:
                    q.append((nx, ny))
                    seen.add((nx, ny))
    return ans
def walk2(x, y, G):
    q = [(x, y)]
    seen = Counter()
    seen[x, y] = 1
    ans = 0
    for x, y in q:
        v = seen[x, y]
        if G[x][y] == 9:
            ans += v
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < len(G) and 0 <= ny < len(G[0]) and G[nx][ny] == 1 + G[x][y]:
                if (nx, ny) not in seen:
                    q.append((nx, ny))
                seen[nx, ny] += v
    return ans
def p1(v):
    G = [[int(x) for x in ln] for ln in get_lines(v)]
    ans = 0
    for x in range(len(G)):
        for y in range(len(G[x])):
            if G[x][y] == 0:
                ans += walk1(x, y, G)
    return ans

def p2(v):
    G = [[int(x) for x in ln] for ln in get_lines(v)]
    ans = 0
    for x in range(len(G)):
        for y in range(len(G[x])):
            if G[x][y] == 0:
                ans += walk2(x, y, G)
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
