#!/usr/bin/python3
import sys, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
from grid import Grid, Pos
import heapq

def get_day(): return 23
def get_year(): return 2024

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def max_clique(nodes, edges):
    deg = Counter()
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    print(sorted(deg.items(), key=lambda x: -x[1]))
def testClique(adj, candidate):
    for u in candidate:
        for v in candidate:
            if u == v: continue
            if v not in adj[u]:
                return False
    return True
def p1(v):
    save_input(v)
    lns = get_lines(v)
    ans = 0
    nodes = set()
    edgs = set()
    for ln in lns:
        a, b = ln.split('-')
        nodes.add(a)
        nodes.add(b)
        edgs.add((a, b))
        edgs.add((b, a))
    L = list(nodes)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if (L[i], L[j]) not in edgs: continue
            for k in range(j+1, len(L)):
                if (L[j], L[k]) in edgs and (L[k], L[i]) in edgs:
                    if 't' in [L[i][0], L[j][0], L[k][0]]:
                        ans += 1
    return ans

def p2(v):
    save_input(v)
    lns = get_lines(v)
    nodes = set()
    adj = defaultdict(set)
    for ln in lns:
        a, b = ln.split('-')
        nodes.add(a)
        nodes.add(b)
        adj[a].add(b)
        adj[b].add(a)
    L = list(nodes)
    for u in L:
        component = adj[u] | {u}
        neigh = adj[u]
        comps = [(len(adj[u]), u)]
        for v in neigh:
            comps.append((len(adj[v] & component), v))
        comps.sort(reverse=True)
        C = [n for _, n in comps[:-1]]
        C.sort()
        if testClique(adj, C):
            return ','.join(C)
    return

LAST_INPUT = None
def save_input(v):
    global LAST_INPUT
    LAST_INPUT = v

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
