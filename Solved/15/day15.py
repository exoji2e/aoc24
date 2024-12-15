#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 15
def get_year(): return 2024

def push(G, pos, dx, dy):
    np = oNp = pos[0] + dx, pos[1] + dy
    while G[np[0]][np[1]] == 'O':
        np = np[0] + dx, np[1] + dy
    if G[np[0]][np[1]] == '#':
        return pos
    assert G[np[0]][np[1]] == '.', f'{G[np[0]][np[1]]}, {np}, {pos}, {dx}, {dy}'
    if oNp == np:
        G[np[0]][np[1]] = '@'
        G[pos[0]][pos[1]] = '.'
        return np
    else:
        G[oNp[0]][oNp[1]] = '@'
        G[np[0]][np[1]] = 'O'
        G[pos[0]][pos[1]] = '.'
        return oNp

def pushH(G, pos, dx, dy):
    assert dx == 0
    np = oNp = pos[0], pos[1] + dy
    toMove = [pos]
    while G[np[0]][np[1]] in '[]':
        toMove.append(np)
        np = np[0], np[1] + dy
    if G[np[0]][np[1]] == '#':
        return pos
    for x, y in toMove[::-1]:
        G[x][y+dy] = G[x][y]
        G[x][y] = '.'
    return oNp
def pushV(G, pos, dx, dy):
    assert dy == 0
    yS = set([pos[1]])
    oNp = pos[0] + dx, pos[1]
    xP = pos[0] + dx
    toMove = [pos]
    while True:
        if any(G[xP][y] not in '[].'  for y in yS):
            break
        if all(G[xP][y] == '.' for y in yS):
            break
        nY = set()
        for y in yS:
            if G[xP][y] == '[':
                nY.add(y+1)
                nY.add(y)
                if (xP, y) not in toMove:
                    toMove.append((xP, y))
                if (xP, y+1) not in toMove:
                    toMove.append((xP, y+1))
            if G[xP][y] == ']':
                nY.add(y-1)
                nY.add(y)
                if (xP, y) not in toMove:
                    toMove.append((xP, y))
                if (xP, y-1) not in toMove:
                    toMove.append((xP, y-1))
        yS = nY
        xP += dx
    if any(G[xP][y] == '#' for y in yS):
        return pos
    for x, y in toMove[::-1]:
        G[x+dx][y] = G[x][y]
        G[x][y] = '.'
    return oNp

def newGrid(G):
    G2 = []
    for l in G:
        l = l.replace('#', '##')
        l = l.replace('O', '[]')
        l = l.replace('.', '..')
        l = l.replace('@', '@.')
        G2.append(list(l))
    return G2

def p1(v):
    chunks = v.split('\n\n')
    G = [list(l) for l in chunks[0].split('\n')]
    instr = chunks[1]
    pos = None
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == '@':
                pos = i, j
    for ins in instr:
        if ins == '>':
            pos = push(G, pos, 0, 1)
        if ins == '<':
            pos = push(G, pos, 0, -1)
        if ins == '^':
            pos = push(G, pos, -1, 0)
        if ins == 'v':
            pos = push(G, pos, 1, 0)
    ans = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == 'O':
                ans += 100*i + j
    return ans

def p2(v):
    chunks = v.split('\n\n')
    G = newGrid(chunks[0].split('\n'))
    instr = chunks[1]
    pos = None
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == '@':
                pos = i, j
    for i, ins in enumerate(instr):
        if ins == '>':
            pos = pushH(G, pos, 0, 1)
        if ins == '<':
            pos = pushH(G, pos, 0, -1)
        if ins == '^':
            pos = pushV(G, pos, -1, 0)
        if ins == 'v':
            pos = pushV(G, pos, 1, 0)
    
    ans = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == '[':
                ans += 100*i + j
    return ans

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
