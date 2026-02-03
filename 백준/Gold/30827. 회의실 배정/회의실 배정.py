[n, k], *l = [[*map(int, i.split())] for i in open(0)]
l.sort(key=lambda x: (x[1], x[0]))
r = [0] * k
a = 0
for s, e in l:
    idx = m = -1
    for i in range(k):
        if m < r[i] < s: m = r[i]; idx = i
    if idx >= 0: r[idx] = e; a += 1
print(a)