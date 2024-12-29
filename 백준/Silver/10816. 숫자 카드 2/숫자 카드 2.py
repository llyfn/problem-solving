import collections as c
_, a, _, b = [input().split() for _ in range(4)]
a = {k: v for k, v in c.Counter(a).items()}
print(*[a.get(i, 0) for i in b])
