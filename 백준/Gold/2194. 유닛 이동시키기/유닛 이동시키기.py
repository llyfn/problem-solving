from collections import deque

[n, m, a, b, k], *l, [sr, sc], [er, ec] = [[*map(int, i.split())] for i in open(0)]
obs = [[0] * m for _ in range(n)]
for r, c in l: obs[r - 1][c - 1] = 1
ps = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        ps[i+1][j+1] = obs[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
v = [[False] * m for _ in range(n)]
v[sr - 1][sc - 1] = True
q = deque([(0, sr - 1, sc - 1)])
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    s, r, c = q.popleft()
    if (r, c) == (er - 1, ec - 1): print(s); break
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr <= n - a and 0 <= nc <= m - b and not v[nr][nc] and ps[nr+a][nc+b] - ps[nr][nc+b] - ps[nr+a][nc] + ps[nr][nc] == 0: v[nr][nc] = True; q.append((s + 1, nr, nc))
else: print(-1)