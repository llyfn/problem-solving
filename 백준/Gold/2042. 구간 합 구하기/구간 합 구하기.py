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
    i += p - 1
    d = v - tree[i]
    while i: tree[i] += d; i //= 2

def isum(l, r):
    a = 0
    l += p - 1; r += p - 1
    while l < r:
        if l & 1: a += tree[l]
        if not r & 1: a += tree[r]
        l = (l + 1) // 2
        r = (r - 1) // 2
    if l == r: a += tree[l]
    return a

for _ in range(m + k):
    a, b, c = map(int, I().split())
    if a == 1: update(b, c)
    else: print(isum(b, c))