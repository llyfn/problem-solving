for _ in range(int(input())):
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    for i in range(1, 33):
        for j in range(k, 0, -1): dp[j] = dp[j - 1] + 1 + dp[j]
        if dp[k] >= n: print(i); break;
    else: print("Impossible")