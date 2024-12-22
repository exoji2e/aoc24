#!/usr/bin/python3
import sys
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 22
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def nextSecret(number):
    v = (number^(number*64)) % 16777216
    v2 = (v^(v//32)) % 16777216
    v3 = (v2^(v2*2048)) % 16777216
    return v3

def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        x = int(ln)
        for _ in range(2000):
            x = nextSecret(x)
        ans += x
    return ans

def p2(v):
    lns = get_lines(v)
    TOT = Counter()
    for ln in lns:
        S = {}
        x = int(ln)
        vs = []
        for _ in range(2000):
            ox = x
            x = nextSecret(x)
            vs.append((x%10) - (ox%10))
            curr = x%10
            if len(vs) >= 4:
                t = tuple(vs[-4:])
                if t not in S:
                    S[t] = curr
        for t, v in S.items():
            TOT[t] += v
    return max(TOT.values())

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
