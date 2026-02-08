from heapq import *
[n], *l = [[*map(int, i.split())] for i in open(0)]
h = v = med = 0
m, M = [], []
for x, y in l:
    h += abs(x)
    if len(m) < len(M): heappush(m, y)
    else: heappush(M, -y)
    if m and M and m[0] < -M[0]: i, j = heappop(m), heappop(M); heappush(M, -i); heappush(m, -j)
    v += abs((med + M[0]) * (not len(m) - len(M))) + abs(y + M[0])
    med = -M[0]
    print(-M[0], h + v)