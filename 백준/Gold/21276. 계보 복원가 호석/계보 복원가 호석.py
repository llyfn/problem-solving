[n], names, [m], *edges = [i.split() for i in open(0)]
n, m = int(n), int(m)
names.sort()
idx = {v: i for i, v in enumerate(names)}
adj = [[] for _ in range(n)]
deg = [0] * n
for u, v in edges:
    adj[idx[v]].append(idx[u])
    deg[idx[u]] += 1

roots = [names[i] for i in range(n) if deg[i] == 0]
print(len(roots))
print(*roots)
for i in range(n):
    kids = sorted(names[c] for c in adj[i] if deg[c] == deg[i] + 1)
    print(names[i], len(kids), *kids)