n, *l = map(int, open(0).read().split())
f = l.index(max(l))
p = [v for i, v in enumerate(l) if f < i < n - 1 and v % 10 == 5 and l[i + 1] < v]
print(sum(x > max(p) for x in l) + 1 if p else 0)