from collections import deque

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
vstd = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]

size = []
q = deque()
for x in range(n):
    for y in range(m):
        length = 1
        if graph[x][y] == 1 and vstd[x][y] == 0:
            q.append([x, y])
            vstd[x][y] = 1
            while q:
                u, v = q.popleft()
                for i in range(4):
                    nu, nv = u + dx[i], v + dy[i]
                    if 0 <= nu < n and 0 <= nv < m and vstd[nu][nv] == 0 and graph[nu][nv] == 1:
                        q.append([nu, nv])
                        vstd[nu][nv] = 1
                        length += 1
            size.append(length)

print(max(size))