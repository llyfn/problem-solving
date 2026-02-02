r, c, *l = open(0).read().split()
r, c = int(r), int(c)
sw = [[0] * (c + 1) for _ in range(r + 1)]
se = [[0] * (c + 1) for _ in range(r + 1)]
for i in range(r - 1, -1, -1):
    for j in range(c):
        if l[i][j] == '1': sw[i][j] = sw[i + 1][j - 1] + 1 if j > 0 else 1; se[i][j] = se[i + 1][j + 1] + 1
ans = 0
for i in range(r):
    for j in range(c):
        for k in range(min(sw[i][j], se[i][j]), ans, -1):
            if se[i + k - 1][j - k + 1] >= k and sw[i + k - 1][j + k - 1] >= k: ans = max(ans, k); break
print(ans)