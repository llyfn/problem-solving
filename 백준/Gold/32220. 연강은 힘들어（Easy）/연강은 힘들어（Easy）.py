n, k, *A = map(int, open(0).read().split())
A = [0, *A, 0]
mod = 10 ** 9 + 7
def cnt(m):
    dp = [0] * (n + 2)
    dp[0] = s = 1
    for i in range(1, n + 2):
        if i > m + 1: s = (s - dp[i - m - 2]) % mod
        if A[i]: dp[i] = 0
        else: dp[i] = s
        s = (s + dp[i]) % mod
    return dp[n + 1]
print((cnt(k) - cnt(k - 1)) % mod)
