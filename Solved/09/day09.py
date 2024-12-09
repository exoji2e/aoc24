#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 9
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

import heapq
def p1(v):
    lns = get_lines(v)
    ln = [int(x) for x in lns[0]]
    arr = []
    pq = []
    for i in range(len(ln)):
        if i%2 == 0:
            for _ in range(ln[i]):
                arr.append(i//2)
        else:
            for _ in range(ln[i]):
                arr.append(-1)
                heapq.heappush(pq, len(arr)-1)
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != -1 and pq and pq[0] < i:
            v = heapq.heappop(pq)
            arr[v] = arr[i]
            arr[i] = -1
    cs = 0
    for i, v in enumerate(arr):
        if v != -1:
            cs += i*v
    return cs

def p2(v):
    lns = get_lines(v)
    ln = [int(x) for x in lns[0]]
    pos = 0
    arr = []
    heaps = [[] for _ in range(10)]
    POS = {}
    for i in range(len(ln)):
        if i%2 == 0:
            arr.append((pos, ln[i], i//2))
            POS[i//2] = pos, ln[i]
            pos += ln[i]
        else:
            heapq.heappush(heaps[ln[i]], pos)
            pos += ln[i]
    
    for i in range(len(arr) - 1, -1, -1):
        pos, v, id = arr[i]
        minPos = pos, -1
        for j in range(v, 10):
            if heaps[j] and heaps[j][0] < minPos[0]:
                minPos = heaps[j][0], j
        if minPos[1] == -1: continue
        x = minPos[0]
        L = minPos[1]
        left = L - v
        heapq.heappop(heaps[L])
        if left > 0:
            heapq.heappush(heaps[left], x + v)
        POS[id] = x, v
    
    cs = 0
    for id, (pos, ln) in POS.items():
        for i  in range(pos, pos + ln):
            cs += id*i
    return cs

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
