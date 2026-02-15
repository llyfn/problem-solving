from collections import *

n, m, *A = map(int, open(0).read().split())
q = deque(range(1, n + 1))
r = 0
for a in A:
    r += min(idx := q.index(a), len(q) - idx)
    q.rotate(-idx)
    q.popleft()
print(r)