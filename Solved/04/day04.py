#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 4
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    G = get_lines(v)
    R,C = len(G), len(G[0])
    def get(r, c):
        if 0 <= r < R and 0 <= c < C:
            return G[r][c]
        return '.'
    cnt = 0
    for r in range(R):
        for c in range(C):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    word = ''.join(get(r+x*i, c+x*j) for x in range(4))
                    if word == 'XMAS':
                        cnt += 1
    return cnt

def p2(v):
    G = get_lines(v)
    R,C = len(G), len(G[0])
    def get(r, c):
        if 0 <= r < R and 0 <= c < C:
            return G[r][c]
        return '.'
    cnt = 0
    for r in range(R):
        for c in range(C):
            if get(r, c) == 'A':
                A, B = get(r-1, c-1), get(r+1, c+1)
                A2, B2 = get(r-1, c+1), get(r+1, c-1)
                v1 = A+B
                v2 = A2+B2
                if (v1 == 'MS' or v1 == 'SM') and (v2 == 'MS' or v2 == 'SM'):
                    cnt += 1

    return cnt

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
