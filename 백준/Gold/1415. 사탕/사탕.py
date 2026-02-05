from collections import *
_, *C = map(int, open(0))
S = sum(C)
C = Counter(C)
N = len(C)
dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1
n = 0
for c in C:
    for s in range(S + 1):
        dp[n + 1][s] = dp[n][s]
        for i in range(1, C[c] + 1):
            if i * c > s: break
            dp[n + 1][s] += dp[n][s - i * c]
    n += 1
p = [1] * (S + 1)
p[0] = 0
if S: p[1] = 0
for i in range(2, int(S ** .5) + 1):
    if p[i]:
        for j in range(2 * i, S + 1, i): p[j] = 0
print(sum(dp[N][i] for i in range(S + 1) if p[i]))