from collections import Counter
_, *C = map(int, open(0))
S = sum(C)
C = Counter(C)
Z = C.pop(0, 0)
dp = [0] * (S + 1)
dp[0] = 1
for p, c in C.items():
    T = [0] * (S + 1)
    for r in range(p):
        v = 0
        for i in range(r, S + 1, p):
            v += dp[i]
            if i >= (c + 1) * p: v -= dp[i - (c + 1) * p]
            T[i] = v
    dp = T
P = [1] * (S + 1)
P[0] = 0
if S: P[1] = 0
for i in range(2, int(S ** .5) + 1):
    if P[i]:
        for j in range(i * i, S + 1, i):
            P[j] = 0
print(sum(dp[i] for i in range(S + 1) if P[i]) * (Z + 1))