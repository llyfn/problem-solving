n, m = map(int, input().split())
p = [input() for _ in range(n)]
q = {i: j for j, i in enumerate(p)}
p = {j: i for j, i in enumerate(p)}
for _ in range(m):
    if (s := input()).isdigit(): print(p[int(s) - 1])
    else: print(q[s] + 1)