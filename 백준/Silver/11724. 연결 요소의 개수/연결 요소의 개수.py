import sys
sys.setrecursionlimit(10**5)
I = lambda: map(int, sys.stdin.readline().split())
n, m = I()
e = [I() for _ in range(m)]
g = [[] for _ in range(n)]
for a, b in e: g[a-1] += b-1,; g[b-1] += a-1,
w = [0] * n
def dfs(v): w[v] = 1; [dfs(i) for i in g[v] if not w[i]]
c = [dfs(v) for v in range(n) if not w[v]]
print(len(c))
