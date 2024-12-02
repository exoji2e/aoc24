#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 2
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def safe(num):
    all_inc = True
    all_dec = True
    max_diff = 0
    min_diff = 10**9
    for i in range(1, len(num)):
        if num[i] < num[i-1]:
            all_inc = False
        if num[i] > num[i-1]:
            all_dec = False
        max_diff = max(max_diff, abs(num[i] - num[i-1]))
        min_diff = min(min_diff, abs(num[i] - num[i-1]))
    return (all_inc or all_dec) and max_diff <= 3 and min_diff >= 1

def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        num = parse(ln)
        if safe(num):
            ans += 1
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        num = parse(ln)
        ok = False
        for i in range(len(num)):
            num2 = num[:i] + num[i+1:]
            if safe(num2):
                ok = True
                break
        if ok:
            ans += 1
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
