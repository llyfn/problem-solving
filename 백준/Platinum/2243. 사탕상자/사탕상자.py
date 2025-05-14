import sys

I = lambda: map(int, sys.stdin.readline().split())
N, = I()
st = [0] * 2 ** 22

def find(n, s, e, c):
    st[n] -= 1
    if s == e: return s
    m = (s + e) // 2
    if st[2 * n] >= c: return find(2 * n, s, m, c)
    else: return find(2 * n + 1, m + 1, e, c - st[2 * n])

def update(n, s, e, i, d):
    st[n] += d
    if s == e: return
    m = (s + e) // 2
    if i <= m: update(2 * n, s, m, i, d)
    else: update(2 * n + 1, m + 1, e, i, d)

for _ in range(N):
    op, *a = I()
    if op == 1: print(find(1, 1, 10 ** 6, a[0]))
    else: update(1,1, 10 ** 6, a[0], a[1])
