from math import ceil, log2
import sys

I = sys.stdin.readline
M = 1_000_000_007
n, m, k = map(int, I().split())
L = [int(I()) for _ in range(n)]

p = pow(2, ceil(log2(n)))
tree = [0] * (2 * p)
for i in range(n): tree[p + i] = L[i]
for i in range(p - 1, 0, -1): tree[i] = tree[2 * i] * tree[2 * i + 1] % M

def update(i, v):
    i += p - 1
    tree[i] = v
    while i > 1: i //= 2; tree[i] = tree[2 * i] * tree[2 * i + 1] % M

def iprod(l, r):
    a = 1
    l += p - 1; r += p - 1
    while l < r:
        if l & 1: a = a * tree[l] % M
        if not r & 1: a = a * tree[r] % M
        l = (l + 1) // 2
        r = (r - 1) // 2
    if l == r: a = a * tree[l] % M
    return a

for _ in range(m + k):
    a, b, c = map(int, I().split())
    if a == 1: update(b, c)
    else: print(iprod(b, c))