from collections import *
for _ in range(int(input())):
    _ = int(input())
    A = [*map(int, input().split())]
    S = sum(A)
    A = [*Counter(A).items()]
    n = len(A)
    dp = [[0] * (S + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(S + 1):
            a, cnt = A[i]
            dp[i + 1][j] = sum(dp[i][j - a * k] for k in range(cnt + 1) if j >= a * k)
    print(sum(dp[n][i] for i in range(S + 1) if sum(str(i).count(d) for d in "13579") % 2))