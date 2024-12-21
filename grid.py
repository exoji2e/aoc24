DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
from collections import namedtuple
class Pos:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def fromTuple(t):
        return Pos(t[0], t[1])
    def neighbors(self):
        for delta in DIRS:
            yield self + delta
    def __add__(self, other):
        if not isinstance(other, Pos):
            return Pos(self.r + other[0], self.c + other[1])
        return Pos(self.r + other.r, self.c + other.c)
    def __sub__(self, other):
        if not isinstance(other, Pos):
            return Pos(self.r - other[0], self.c - other[1])
        return Pos(self.r - other.r, self.c - other.c)
    def __eq__(self, other):
        if not isinstance(other, Pos):
            try:
                return self.r == other[0] and self.c == other[1]
            except:
                return False
        return self.r == other.r and self.c == other.c
    def __lt__(self, other):
        return (self.r, self.c) < (other.r, other.c)
    def __hash__(self):
        return hash((self.r, self.c))
    def __repr__(self):
        return f'({self.r}, {self.c})'
    def __iter__(self):
        return iter((self.r, self.c))
    def __getitem__(self, idx):
        return (self.r, self.c)[idx]

from collections import *
class Grid:
    def __init__(self, lines):
        self.R = len(lines)
        self.W = len(lines[0])
        self.g = [list(l) for l in lines]
    
    def fromSize(R, C, char):
        return Grid([[char for _ in range(C)] for _ in range(R)])
    
    '''
    neigh_fn is a function from (pos, grid) to a list of new_positions
    pass T to get distance to T, 
    otherwise returns a dict of distances to all reachable positions
    '''
    def bfs(self, S, T=None, neigh_fn=None):
        INF = 10**18
        if neigh_fn is None:
            neigh_fn = lambda p, self: self.neighbors(p)
        dist = defaultdict(lambda: INF)
        q = [Pos.fromTuple(S)]
        dist[q[0]] = 0
        for p in q:
            if p == T:
                break
            for n in neigh_fn(p, self):
                if n not in dist:
                    dist[n] = dist[p] + 1
                    q.append(n)
        if T != None:
            d = dist[Pos.fromTuple(T)]
            return -1 if d == INF else d
        return dist

    '''
    neigh_fn is a function from (pos, grid) to a list of (new_pos, weight) pairs
    pass T to get distance to T, 
    otherwise returns a dict of distances to all reachable positions
    '''
    def dijkstra(self, S, T=None, neigh_fn=None):
        import heapq
        INF = 10**18
        if neigh_fn is None:
            neigh_fn = lambda p, self: [(n, 1) for n in self.neighbors(p)]
        dist = defaultdict(lambda: INF)
        pq = []
        def add(node, dst):
            if dst < dist[node]:
                dist[node] = dst
                heapq.heappush(pq, (dst, node))
        add(Pos.fromTuple(S), 0)

        while pq:
            D, u = heapq.heappop(pq)
            if u == T: return D
            if D != dist[u]: continue
            for v, w in neigh_fn(u, self):
                add(v, D + w)
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
    def __setitem__(self, p, val):
        if isinstance(p, int):
            self.g[p] = val
            return
        if isinstance(p, tuple):
            p = Pos.fromTuple(p)
        self.g[p.r][p.c] = val
        