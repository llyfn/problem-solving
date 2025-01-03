from math import ceil, log2
import sys

I = sys.stdin.readline
n, m, k = map(int, I().split())
L = [int(I()) for _ in range(n)]

p = pow(2, ceil(log2(n)))
tree = [0] * (2 * p)
tree[p:p+n] = L
aux = [0] * (2 * p)
for i in range(p - 1, 0, -1): tree[i] = tree[2 * i] + tree[2 * i + 1]

def update(l, r, d, i, s, e):
    update_aux(i, s, e)
    if r < s or e < l: return
    if l <= s and e <= r:
        tree[i] += d * (e - s + 1)
        if s != e: aux[2 * i] += d; aux[2 * i + 1] += d
        return
    mid = (s + e) >> 1
    update(l, r, d, 2 * i, s, mid)
    update(l, r, d, 2 * i + 1, mid + 1, e)
    tree[i] = tree[2 * i] + tree[2 * i + 1]

def isum(l, r, i, s, e):
    update_aux(i, s, e)
    if r < s or e < l: return 0
    if l <= s and e <= r: return tree[i]
    mid = (s + e) >> 1
    return isum(l, r, 2 * i, s, mid) + isum(l, r, 2 * i + 1, mid + 1, e)

def update_aux(i, s, e):
    if aux[i]:
        tree[i] += aux[i] * (e - s + 1)
        if s != e: aux[2 * i] += aux[i]; aux[2 * i + 1] += aux[i]
        aux[i] = 0

for _ in range(m + k):
    a, *b = map(int, I().split())
    if a == 1: update(b[0], b[1], b[2], 1, 1, p)
    else: print(isum(b[0], b[1], 1, 1, p))