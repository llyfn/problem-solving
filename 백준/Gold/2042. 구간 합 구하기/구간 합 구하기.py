from math import ceil, log2
import sys

I = sys.stdin.readline
n, m, k = map(int, I().split())
L = [int(I()) for _ in range(n)]

p = pow(2, ceil(log2(n)))
tree = [0] * (2 * p)
for i in range(n): tree[p + i] = L[i]
for i in range(p - 1, 0, -1): tree[i] = tree[2 * i] + tree[2 * i + 1]

def update(i, v):
    idx = p + i - 1
    d = v - tree[idx]
    while idx: tree[idx] += d; idx //= 2

def isum(l, r):
    a = []
    s, e = p + l - 1, p + r - 1
    while s < e:
        if s & 1: a += tree[s],
        if not e & 1: a += tree[e],
        s = (s + 1) // 2
        e = (e - 1) // 2
    if s == e: a += tree[s],
    return sum(a)

for _ in range(m + k):
    a, b, c = map(int, I().split())
    if a == 1: update(b, c)
    else: print(isum(b, c))