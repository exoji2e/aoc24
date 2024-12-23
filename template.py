#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return datetime.date.today().day
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def p1(v):
    save_input(v)
    lns = get_lines(v)
    chunks = v.split('\n\n')
    ans = 0
    for ln in lns:
        item = parse(ln)
        ans += 0
    return ans

def p2(v):
    return p1(v)

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
