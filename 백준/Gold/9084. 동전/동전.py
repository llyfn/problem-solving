for _ in range(int(input())):
    n = int(input())
    v = [*map(int, input().split())]
    m = int(input())
    dp = [[1] + [0] * m] * 2
    for c in range(n):
        p = c % 2; q = +(not p)
        if c > 0: dp[p] = dp[q][:]
        for i in range(c, m + 1):
            if i >= v[c]: dp[p][i] += dp[p][i - v[c]]
    print(dp[not n % 2][-1])
