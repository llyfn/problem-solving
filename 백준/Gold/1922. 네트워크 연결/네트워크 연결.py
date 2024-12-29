from heapq import *

def prim(start, edges):
    connected = set([start])
    cost = 0

    candidateEdges = edges[start]
    heapify(candidateEdges)

    while candidateEdges:
        c, v = heappop(candidateEdges)
        if v not in connected:
            connected.add(v)
            cost += c

            for edge in graph[v]:
                if edge[1] not in connected:
                    heappush(candidateEdges, edge)
    
    return cost

n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().strip().split())
    graph[u-1].append((c, v-1))
    graph[v-1].append((c, u-1))

print(prim(0, graph))