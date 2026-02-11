a, b, k = map(int, input().split())
D = set()
s = a + b
for i in range(1, int(s ** .5) + 1):
    if s % i == 0: D.add(i); D.add(s // i)
for d in sorted(D, reverse=True):
    if min(a % d, d - a % d) <= k: print(d); break