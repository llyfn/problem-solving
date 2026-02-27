from collections import *
import sys
input = sys.stdin.readline
n = int(input())
s = n * n
graph = [[] for _ in range(s)]
deg = [0] * s
def add_edge(u, v): graph[u].append(v); deg[v] += 1
for i in range(n):
    for j, op in enumerate(input().split()):
        u, v = i * n + j, i * n + j + 1
        add_edge(u, v) if op == '<' else add_edge(v, u)
for i in range(n - 1):
    for j, op in enumerate(input().split()):
        u, v = i * n + j, (i + 1) * n + j
        add_edge(u, v) if op == '<' else add_edge(v, u)
q = deque([i for i in range(s) if not deg[i]])
ans = [0] * s
r = 0
while q:
    u = q.popleft()
    ans[u] = (r := r + 1)
    for v in graph[u]:
        deg[v] -= 1
        if not deg[v]: q.append(v)
for i in range(0, s, n): print(*ans[i:i + n])