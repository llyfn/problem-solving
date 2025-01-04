from math import ceil, log2
import sys

I = lambda: map(int, sys.stdin.readline().split())

def update(x, y, d):
    while x <= n:
        yy = y
        while yy <= n:
            tree[x][yy] += d
            yy += yy & -yy
        x += x & -x

def isum(x1, y1, x2, y2):
    return cal(x2, y2) - cal(x1 - 1, y2) - cal(x2, y1 - 1) + cal(x1 - 1, y1 - 1)

def cal(x, y):
    s = 0
    while x:
        yy = y
        while yy:
            s += tree[x][yy]
            yy -= yy & -yy
        x -= x & -x
    return s

n, m = I()
L = [[]] + [[0, *I()] for _ in range(n)]
tree = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1): update(i, j, L[i][j])

for _ in range(m):
    w, *l = I()
    if w: print(isum(*l))
    else:
        x, y, v = l
        update(x, y, v - L[x][y])
        L[x][y] = v
