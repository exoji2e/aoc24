#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 24
def get_year(): return 2024

def parse(ln):
    arr = ln.split(' ')
    g1, g2 = arr[0], arr[2]
    op = arr[1]
    target = arr[-1]
    return min(g1, g2), max(g1, g2), op, target

def init(x, y):
    xv = list(map(int, bin(x)[2:]))[::-1]
    yv = list(map(int, bin(y)[2:]))[::-1]
    values = {}
    for i in range(45):
        iS = str(i) if i >= 10 else '0' + str(i)
        if i == 0: iS = '00'
        if i < len(xv):
            values[f'x{iS}'] = xv[i]
        else:
            values[f'x{iS}'] = 0
        if i < len(yv):
            values[f'y{iS}'] = yv[i]
        else:
            values[f'y{iS}'] = 0
    return values

def test(x, y, gates):
    values = init(x, y)
    #desc = {k : k for k in values}
    desc = None
    ch = True
    while ch:
        ch = False
        for g1, g2, op, c in gates:
            if c in values: continue
            if g1 not in values: continue
            if g2 not in values: continue
            a, b = values[g1], values[g2]
            # d1 = desc[g1]
            # d2 = desc[g2]
            # d1, d2 = max(d1, d2), min(d1, d2)
            if op == 'AND':
                values[c] = a & b
            #     desc[c] = f'({d1} AND {d2})'
            elif op == 'OR':
                values[c] = a | b
            #     desc[c] = f'({d1} OR {d2})'
            elif op == 'XOR':
                values[c] = a ^ b
            #     desc[c] = f'({d1} XOR {d2})'
            else:
                assert 0
            ch = True
    lst = sorted(values.items(), reverse=True)
    
    zs = [v for k, v in lst if k[0] == 'z']
    return int(''.join(map(str, zs)), 2), desc
# z05 wrong
def gateSwap(gates, swaps):
    newG = []
    for g in gates:
        g1, g2, op, c = g
        if c in swaps:
            c = swaps[c]
        newG.append((g1, g2, op, c))
    return newG
def findFirstErr(gates, delta):
    E = 10**10
    for i in range(30):
        x = random.randint(0, 2**44)
        y = random.randint(0, 2**44)
        z = test(x, y, gates)[0]
        real = x + y
        xorDiff = z ^ real
        if xorDiff == 0: continue
        firstIdx = 0
        while xorDiff & (1 << firstIdx) == 0:
            firstIdx += 1
        E = min(E, firstIdx)
        if E <= delta: return E
    return E
import random
def p1(v):
    chunks = v.split('\n\n')
    start = chunks[0].split('\n')
    gatesStrs = chunks[1].split('\n')
    gates = [parse(gate) for gate in gatesStrs]

    values = {}
    desc = {}
    for ln in start:
        x, y = ln.split(': ')
        values[x] = int(y)
        desc[x] = x
    ch = True
    
    while ch:
        ch = False
        for g1, g2, op, c in gates:
            if c in values: continue
            if g1 not in values: continue
            if g2 not in values: continue
            a, b = values[g1], values[g2]
            d1 = desc[g1]
            d2 = desc[g2]
            d1, d2 = max(d1, d2), min(d1, d2)
            if op == 'AND':
                values[c] = a & b
                desc[c] = f'({d1} AND {d2})'
            elif op == 'OR':
                values[c] = a | b
                desc[c] = f'({d1} OR {d2})'
            elif op == 'XOR':
                values[c] = a ^ b
                desc[c] = f'({d1} XOR {d2})'
            else:
                assert 0
            ch = True
    lst = sorted(values.items(), reverse=True)
    zs = [v for k, v in lst if k[0] == 'z']
    return int(''.join(map(str, zs)), 2)

def p2(v):
    chunks = v.split('\n\n')
    start = chunks[0].split('\n')
    gatesStrs = chunks[1].split('\n')
    gates = [parse(gate) for gate in gatesStrs]

    pairs = [] #[['z15', 'kqk'], ['svm', 'nbc']]
    MAP = {}
    for a, b in pairs:
        MAP[a] = b
        MAP[b] = a
    gates = gateSwap(gates, MAP)
    
    currErr = findFirstErr(gates, 0)
    print('err', currErr)
    gateTargets = {v for _, _, _, v in gates}
    for _ in range(4):
        changed = False
        for a in gateTargets:
            if changed: break
            for b in gateTargets:
                if a == b: continue
                gates2 = gateSwap(gates, {a : b, b : a})
                err = findFirstErr(gates2, currErr)
                if err > currErr:
                    gates = gates2
                    currErr = err
                    pairs.append([a, b])
                    print(err, a, b)
                    if len(pairs) >= 4:
                        words = [v for p in pairs for v in p]
                        return ','.join(sorted(words))
                    break

    return None

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
