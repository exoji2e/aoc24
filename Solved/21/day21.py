#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 21
def get_year(): return 2024

def createMap(G):
    p = {}
    for i, ln in enumerate(G.split('\n')):
        for j, c in enumerate(ln):
            p[c] = i, j
    return p

G = '''
789
456
123
X0A'''

POS = createMap(G)
G2 = '''
X^A
<v>'''
P2 = createMap(G2)


def isPathOK(a, path, P):
    p = [a]
    for c in path:
        if c == '^':
            p.append((p[-1][0] - 1, p[-1][1]))
        if c == 'v':
            p.append((p[-1][0] + 1, p[-1][1]))
        if c == '<':
            p.append((p[-1][0], p[-1][1] - 1))
        if c == '>':
            p.append((p[-1][0], p[-1][1] + 1))
    return P['X'] not in p

def getPaths2(a, b, P):
    p1 = []
    p2 = []
    cA = a
    while cA[0] != b[0]:
        if cA[0] < b[0]:
            p1.append('v')
            cA = cA[0] + 1, cA[1]
        else:
            p1.append('^')
            cA = cA[0] - 1, cA[1]
    while cA[1] != b[1]:
        if cA[1] < b[1]:
            p2.append('>')
            cA = cA[0], cA[1] + 1
        else:
            p2.append('<')
            cA = cA[0], cA[1] - 1
    paths = [p1+p2, p2+p1]
    return [p for p in paths if isPathOK(a, p, P)]

def cost0(T, state):
    return 1
def cost1(T, state):
    sPos = P2[state[1]]
    tPos = P2[T]
    paths = getPaths2(sPos, tPos, P2)
    minC = 10**10
    for p in paths:
        stateClone = state
        c = 0
        for press in p:
            c += cost0(press, stateClone)
            stateClone = (press, *stateClone[1:])
        c += cost0('A', stateClone)
        minC = min(minC, c)
    return minC 
def cost2(T, state):
    sPos = P2[state[2]]
    tPos = P2[T]
    paths = getPaths2(sPos, tPos, P2)
    minC = 10**10
    for p in paths:
        stateClone = state
        c = 0
        for press in p:
            c += cost1(press, stateClone)
            stateClone = ('A', press, *stateClone[2:])
        c += cost1('A', stateClone)
        minC = min(minC, c)
    return minC

def cost3(T, state):
    sPos = POS[state[3]]
    tPos = POS[T]
    paths = getPaths2(sPos, tPos, POS)
    minC = 10**10
    for p in paths:
        stateClone = state
        c = 0
        for press in p:
            c += cost2(press, stateClone)
            stateClone = ('A', 'A', press, *stateClone[3:])
        c += cost2('A', stateClone)
        minC = min(minC, c)
    return minC

DP = {}
def costL(T, S, lvl):
    if lvl == 0:
        return 1
    TUP = (T, S, lvl)
    if TUP in DP:
        return DP[TUP]
    sPos = P2[S]
    tPos = P2[T]
    paths = getPaths2(sPos, tPos, P2)
    minC = 10**18
    for p in paths:
        last = 'A'
        c = 0
        for press in p:
            c += costL(press, last, lvl-1)
            last = press
        c += costL('A', last, lvl-1)
        minC = min(minC, c)
    DP[TUP] = minC
    return minC

def costTOP(T, S, lvl):
    sPos = POS[S]
    tPos = POS[T]
    paths = getPaths2(sPos, tPos, POS)
    minC = 10**18
    for p in paths:
        last = 'A'
        c = 0
        for press in p:
            c += costL(press, last, lvl-1)
            last = press
        c += costL('A', last, lvl-1)
        minC = min(minC, c)
    return minC

def solve1(ln):
    V = 'A' + ln
    su = 0
    for a, b in zip(V, V[1:]):
        c = cost3(b, ('A', 'A', 'A', a))
        su += c
    return su * int(ln[:-1])
def solve2(ln):
    V = 'A' + ln
    su = 0
    for a, b in zip(V, V[1:]):
        c = costTOP(b, a, 26)
        su += c
    return su * int(ln[:-1])


def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        ans += solve1(ln)
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        ans += solve2(ln)
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
