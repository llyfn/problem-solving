import sys
I = lambda: map(int, sys.stdin.readline().split())

n, m = I()
L = [[0] * (n + 1)] + [[0] + [*I()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        L[i + 1][j + 1] += L[i + 1][j] + L[i][j + 1] - L[i][j]

for _ in range(m):
    x1, y1, x2, y2 = I()
    print(L[x2][y2] - L[x2][y1 - 1] - L[x1 - 1][y2] + L[x1 - 1][y1 - 1])
