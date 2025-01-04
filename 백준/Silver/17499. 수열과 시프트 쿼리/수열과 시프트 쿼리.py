import sys

I = lambda: map(int, sys.stdin.readline().split())
n, q = I(); a = [*I()]; s = 0
for _ in range(q):
    q, *v = I()
    if q == 1: a[(v[0] + s - 1) % n] += v[1]
    elif q == 2: s = (s - v[0]) % n
    else: s = (s + v[0]) % n
print(*a[s:], *a[:s])