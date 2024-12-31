v = [1, 5, 10, 25]
z = [0] * 4
x, *c = map(int, input().split())
d = [z[:]] + [0] * x
for i in range(1, x + 1):
    p = z[:]
    for j in range(4):
        k = i - v[j]
        if k < 0 or not d[k]: continue
        if d[k][j] + 1 <= c[j]:
            r = d[k][:]
            r[j] += 1
            if sum(r) > sum(p): p = r
    if sum(p): d[i] = p
print(*d[x] or z)