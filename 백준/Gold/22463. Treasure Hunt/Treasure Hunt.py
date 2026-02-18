from bisect import *

[n, m], *l = [[*map(int, i.split())] for i in open(0)]
T, H = l[:n], l[n:]

ys = sorted(list({t[1] for t in T}))
ylen = len(ys)
bit = [0] * (ylen + 1)
def update(i, d):
    while i <= ylen: bit[i] += d; i += i & (-i)
def query(i):
    s = 0
    while i > 0: s += bit[i]; i -= i & (-i)
    return s

Q = []
for x, y in T: Q.append((x, 0, bisect_left(ys, y) + 1))
ans = [0] * m
for i in range(m):
    x1, y1, x2, y2 = H[i]
    h, l = bisect_right(ys, y2), bisect_left(ys, y1)
    if h > l:
        Q.append((x1 - 1, 1, l, h, i, -1))
        Q.append((x2, 1, l, h, i, 1))
Q.sort()
for q in Q:
    if q[1] == 0: update(q[2], 1)
    else:
        _, _, y_l, y_h, idx, mult = q
        ans[idx] += (query(y_h) - query(y_l)) * mult
print('\n'.join(map(str, ans)))
