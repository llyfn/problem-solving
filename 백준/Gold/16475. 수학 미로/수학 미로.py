from heapq import *
[N, M, K, L, P], traps, *roads, [S, E] = [[*map(int, i.split())] for i in open(0)]
traps = set(traps)
graph = [[] for _ in range(N + 1)]
for a, b, c in roads[:M - L]: graph[a].append((b, c, -1))
for a, b, c in roads[M - L:]: graph[a].append((b, c, 0)); graph[b].append((a, c, 1))
dist = [[1e9] * (2 * P) for _ in range(N + 1)]
dist[S][0] = 0
q = [(0, S, 0)]
while q:
    d, u, s = heappop(q)
    if u == E: print(d); break
    for v, c, t in graph[u]:
        ns = (s + (v in traps)) % (2 * P)
        if (t < 0 or (s >= P) == t) and d + c < dist[v][ns]: heappush(q, (d + c, v, ns)); dist[v][ns] = d + c
else: print(-1)
