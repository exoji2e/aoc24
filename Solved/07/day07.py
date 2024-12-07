#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 7
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' :'))

from itertools import product

def test(arr):
    expr = arr[1:]
    for ops in product('+*', repeat=len(expr)-1):
        acc = expr[0]
        for j in range(len(expr)-1):
            if ops[j] == '+':
                acc += expr[j+1]
            else:
                acc *= expr[j+1]
        if acc == arr[0]:
            return acc
    return 0

def test2(arr):
    expr = arr[1:]
    for ops in product('|+*', repeat=len(expr)-1):
        acc = expr[0]
        for j in range(len(expr)-1):
            if ops[j] == '+':
                acc += expr[j+1]
            elif ops[j] == '*':
                acc *= expr[j+1]
            else:
                acc = int(str(acc) + str(expr[j+1]))
        if acc == arr[0]:
            return acc
    return 0

def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        item = parse(ln)
        v = test(item)
        ans += v
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        item = parse(ln)
        v = test2(item)
        ans += v
    return ans

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
