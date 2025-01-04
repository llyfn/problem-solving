import sys

I = lambda: map(int, sys.stdin.readline().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(next(I())):
    m, n, k = I()
    l = [[0] * n for _ in range(m)]
    for _ in range(k): x, y = I(); l[x][y] = 1
    q = []; c = 0
    for i in range(m):
        for j in range(n):
            if l[i][j]:
                q += [i, j],; l[i][j] = 0; c += 1
                while q:
                    x, y = q.pop()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < m and 0 <= ny < n and l[nx][ny]:
                            q += [nx, ny],
                            l[nx][ny] = 0
    print(c)
