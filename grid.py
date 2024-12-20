DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Pos:
    def __init__(self, r, c, dir=0):
        self.r = r
        self.c = c
        self.dir = dir
    def fromTuple(t):
        return Pos(t[0], t[1])
    def neighbors(self):
        for dr, dc in DIRS:
            yield self + Pos(dr, dc)
    def forward(self):
        return self + Pos(*DIRS[self.dir])
    def turnLeft(self):
        return Pos(self.r, self.c, (self.dir - 1)%4)
    def turnRight(self):
        return Pos(self.r, self.c, (self.dir + 1)%4)
    def __add__(self, other):
        if isinstance(other, Pos):
            return Pos(self.r + other.r, self.c + other.c, self.dir)
        return Pos(self.r + other[0], self.c + other[1], self.dir)
    def __sub__(self, other):
        return Pos(self.r - other.r, self.c - other.c, self.dir)
    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.r == other[0] and self.c == other[1]
        return self.r == other.r and self.c == other.c
    def __lt__(self, other):
        return (self.r, self.c) < (other.r, other.c)
    def __hash__(self):
        return hash((self.r, self.c, self.dir))
    def __repr__(self):
        return f'({self.r}, {self.c})'
    def __iter__(self):
        return iter((self.r, self.c))
    def __getitem__(self, rc):
        if rc == 0:
            return self.r
        if rc == 1:
            return self.c
        raise IndexError

from collections import *
class Grid:
    def __init__(self, lines):
        self.R = len(lines)
        self.W = len(lines[0])
        self.g = [list(l) for l in lines]
    
    def fromSize(R, C, char):
        return Grid([[char for _ in range(C)] for _ in range(R)])
    
    def bfs(self, S, T=None, neigh_fn=None):
        INF = 10**18
        if neigh_fn is None:
            neigh_fn = lambda p, self: self.neighbors(p)
        dist = defaultdict(lambda: INF)
        q = [Pos.fromTuple(S)]
        dist[q[0]] = 0
        for p in q:
            if p is T:
                break
            for n in neigh_fn(p, self):
                if n not in dist:
                    dist[n] = dist[p] + 1
                    q.append(n)
        if T is not None:
            d = dist[Pos.fromTuple(T)]
            return -1 if d == INF else d
        return dist

    def neighbors(self, p):
        for n in p.neighbors():
            if self.inside(n) and self.g[n.r][n.c] != '#':
                yield n
    def coords(self):
        for r in range(self.R):
            for c in range(self.W):
                yield Pos(r, c)
    def inside(self, p):
        return 0 <= p.r < self.R and 0 <= p.c < self.W
    def find(self, char):
        return next(self.findAll(char))
    def findAll(self, char):
        for p in self.coords():
            if self.g[p.r][p.c] == char:
                yield p
    def getAt(self, p):
        if self.inside(p):
            return self.g[p.r][p.c]
        else:
            return '#'

    def __repr__(self):
        return '\n'.join([''.join(x) for x in self.g])
    def __getitem__(self, rc):
        if isinstance(rc, Pos):
            return self.getAt(rc)
        if isinstance(rc, tuple):
            return self.getAt(Pos(*rc))
        if isinstance(rc, int):
            return self.g[rc]
    def __setitem__(self, rc, val):
        p = rc
        if isinstance(rc, tuple):
            p = Pos(*rc)
        self.g[p.r][p.c] = val
        