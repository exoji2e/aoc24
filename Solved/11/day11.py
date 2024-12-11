#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 11
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    ln = get_lines(v)[0]
    items = parse(ln)
    for _ in range(25):
        newItems = []
        for v in items:
            if v == 0:
                newItems.append(1)
            elif len(str(v))%2 == 0:
                strV = str(v)
                a, b = strV[:len(strV)//2], strV[len(strV)//2:]
                newItems.append(int(a))
                newItems.append(int(b))
            else:
                newItems.append(v*2024)
        items = newItems
    return len(items)

def p2(v):
    ln = get_lines(v)[0]
    items = Counter(parse(ln))
    for _ in range(75):
        newItems = Counter()
        for v, no in items.items():
            if v == 0:
                newItems[1] += no
            elif len(str(v))%2 == 0:
                strV = str(v)
                a, b = strV[:len(strV)//2], strV[len(strV)//2:]
                newItems[int(a)] += no
                newItems[int(b)] += no
            else:
                newItems[v*2024] += no
        items = newItems
    return sum(items.values())


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
