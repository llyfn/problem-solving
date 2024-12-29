from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
vstd = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]

q = deque()
q.append([0,0])
vstd[0][0] = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and vstd[nx][ny] == 0 and graph[nx][ny] == 1:
            q.append([nx, ny])
            vstd[nx][ny] = vstd[x][y] + 1
            

print(vstd[-1][-1])