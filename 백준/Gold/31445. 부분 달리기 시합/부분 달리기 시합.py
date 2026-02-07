[n, m], *l = [[*map(int, i.split())] for i in open(0)]
MOD = 10 ** 9 + 7
graph = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
cnt = [1] * (n + 1)
for x, y in l: graph[x].append(y); deg[y] += 1
ans = 0
q = [i for i in range(1, n + 1) if deg[i] == 0]
while q:
    x = q.pop(0)
    ans = (ans + cnt[x]) % MOD
    nq = []
    v = [0] * (n + 1)
    for y in graph[x]:
        deg[y] -= 1
        if deg[y] == 0: q.append(y)
        if v[y] == 0: v[y] = 1; nq.append(y)
    while nq:
        z = nq.pop(0)
        cnt[z] = (cnt[z] + cnt[x]) % MOD
        for y in graph[z]:
            if v[y] == 0: v[y] = 1; nq.append(y)
print(ans)