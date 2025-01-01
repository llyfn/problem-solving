n, m = map(int, input().split())
d = {k: v for k, v in [input().split() for _ in range(n)]}
for _ in range(m): print(d[input()])