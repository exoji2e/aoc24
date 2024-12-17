#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 17
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

"""
Register A: 44374556
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0
"""
def combo(v, A, B, C):
    if 0 <= v <= 3: return v
    if v == 4: return A
    if v == 5: return B
    if v == 6: return C
    assert 0

def runProg(prog, A, B, C):
    i = 0
    out = []
    while i < len(prog):
        if prog[i] == 0:
            v = combo(prog[i+1], A, B, C)
            A = A//(2**v)
            i+= 2
        elif prog[i] == 1:
            op = prog[i+1]
            B = B^op
            i+= 2
        elif prog[i] == 2:
            op = combo(prog[i+1], A, B, C)
            B = op%8
            i+= 2
        elif prog[i] == 3:
            if A == 0:
                i+= 2
            else:
                i = prog[i+1]
        elif prog[i] == 4:
            B = B^C
            i+=2
        elif prog[i] == 5:
            out.append(combo(prog[i+1], A, B, C)%8)
            i+=2
        elif prog[i] == 6:
            v = combo(prog[i+1], A, B, C)
            B = A//(2**v)
            i+= 2
        elif prog[i] == 7:
            v = combo(prog[i+1], A, B, C)
            C = A//(2**v)
            i+= 2
    return out

def p1(v):
    A = 44374556
    B = 0
    C = 0
    prog = [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0]
    out = runProg(prog, A, B, C)
    return ','.join(map(str, out))


#Program: 2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0
# 2 4 -> bst 4 -> B = A % 8
# 1 5 -> bxl 5 -> B = B ^ 5
# 7 5 -> cdv 5 -> C = A // 2^B
# 1 6 -> bxl 6 -> B = B ^ 6
# 0 3 -> adv 3 -> A = A // 2^3
# 4 1 -> bxc 1 -> B = B ^ C
# 5 5 -> out 5 -> out B % 8
# 3 0 -> jnz 0 -> if A == 0: break
####

# while A != 0:
#     B = A%8 ^ 5
#     C = A//2^B
#     B = B^6
#     B = B^C
#     print(B%8)
#     A = A//2^3
def p2(v):
    B = 0
    C = 0
    prog = [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0]
    lastOK = [0]
    for i in range(len(prog) - 1, -1, -1):
        subProg = prog[i:]
        newOK = set()
        for i in range(8):
            for last in lastOK:
                out = runProg(prog, last*8 + i, B, C)
                if out == subProg:
                    newOK.add(last*8 + i)
        lastOK = newOK
    A = min(lastOK)
    assert runProg(prog, A, B, C) == prog
    return A

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
