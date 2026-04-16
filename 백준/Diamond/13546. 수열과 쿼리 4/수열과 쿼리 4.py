import sys
from collections import deque
from math import isqrt

[n, K], A, [m], *Q = [[*map(int, i.split())] for i in open(0)]
queries = [(Q[i][0] - 1, Q[i][1] - 1, i) for i in range(m)]
block = max(1, isqrt(n))
queries.sort(key=lambda q: (q[0] // block, q[1] if (q[0] // block) & 1 == 0 else -q[1]))
dq = [deque() for _ in range(K + 2)]
diff = [0] * (K + 2)
present = bytearray(K + 2)
cnt = [0] * (n + 2)
cur_max = 0
ans = [0] * m
L, R = 0, -1
for ql, qr, qi in queries:
    while R < qr:
        R += 1
        v = A[R]
        d = dq[v]
        if not present[v]:
            d.append(R)
            present[v] = 1
            cnt[0] += 1
        else:
            d_old = diff[v]
            d.append(R)
            d_new = d[-1] - d[0]
            cnt[d_old] -= 1
            cnt[d_new] += 1
            diff[v] = d_new
            if d_new > cur_max:
                cur_max = d_new
    while L > ql:
        L -= 1
        v = A[L]
        d = dq[v]
        if not present[v]:
            d.append(L)
            present[v] = 1
            cnt[0] += 1
        else:
            d_old = diff[v]
            d.appendleft(L)
            d_new = d[-1] - d[0]
            cnt[d_old] -= 1
            cnt[d_new] += 1
            diff[v] = d_new
            if d_new > cur_max:
                cur_max = d_new
    while R > qr:
        v = A[R]
        d = dq[v]
        d_old = diff[v]
        d.pop()
        if not d:
            present[v] = 0
            cnt[d_old] -= 1
            diff[v] = 0
        else:
            d_new = d[-1] - d[0]
            cnt[d_old] -= 1
            cnt[d_new] += 1
            diff[v] = d_new
        if d_old == cur_max and cnt[d_old] == 0:
            while cur_max > 0 and cnt[cur_max] == 0:
                cur_max -= 1
        R -= 1
    while L < ql:
        v = A[L]
        d = dq[v]
        d_old = diff[v]
        d.popleft()
        if not d:
            present[v] = 0
            cnt[d_old] -= 1
            diff[v] = 0
        else:
            d_new = d[-1] - d[0]
            cnt[d_old] -= 1
            cnt[d_new] += 1
            diff[v] = d_new
        if d_old == cur_max and cnt[d_old] == 0:
            while cur_max > 0 and cnt[cur_max] == 0:
                cur_max -= 1
        L += 1
    ans[qi] = cur_max
sys.stdout.write('\n'.join(map(str, ans)))