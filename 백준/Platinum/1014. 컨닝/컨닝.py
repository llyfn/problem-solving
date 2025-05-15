import sys

d = [(1, -1), (1, 1), (-1, -1), (-1, 1), (0, 1), (0, -1)]

def bipartite(i, j):
    for y, x in G[i][j]:
        if V[y][x]: continue
        V[y][x] = 1
        if not P[y][x] or bipartite(*P[y][x]): P[y][x] = (i, j); return 1
    return 0

for _ in range(int(input())):
    N, M = map(int, sys.stdin.readline().split())
    C = [input() for _ in range(N)]
    G = [[[] for _ in range(M)] for _ in range(N)]
    V, P = [[0] * M for _ in range(N)], [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for dy, dx in d:
                if C[i][j] != '.': continue
                y, x = i + dy, j + dx
                if 0 <= y < N and 0 <= x < M and C[y][x] == '.': G[i][j].append((y, x))
    S = sum(s.count('.') for s in C)
    A = 0
    for i in range(N):
        for j in range(0, M, 2):
            V = [[0] * M for _ in range(N)]
            V[i][j] = 1
            A += bipartite(i, j)
    print(S - A)