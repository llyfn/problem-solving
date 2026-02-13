n, m, *h = map(int, open(0).read().split())
a = 1e6
s = l = 0
for r in range(n):
    s += h[r]
    while s >= m:
        a = min(a, r - l + 1)
        s -= h[l]
        l += 1
print("NEPAVYKS" if a == 1e6 else a)
