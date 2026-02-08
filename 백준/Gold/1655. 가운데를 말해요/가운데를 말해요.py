from heapq import *
n, *l = map(int, open(0))
m, M = [], []
for x in l:
    if len(m) < len(M): heappush(m, x)
    else: heappush(M, -x)
    if m and M and m[0] < -M[0]: i, j = heappop(m), heappop(M); heappush(M, -i); heappush(m, -j)
    print(-M[0])