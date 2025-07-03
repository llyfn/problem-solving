import sys
input = sys.stdin.readline
M = 10 ** 9 + 7
N = 4 * 10 ** 6
fact = [1] * (N + 1)
for i in range(1, N + 1): fact[i] = fact[i - 1] * i % M
inv_fact = [1] * (N + 1)
inv_fact[N] = pow(fact[N], M - 2, M)
for i in range(N - 1, -1, -1): inv_fact[i] = inv_fact[i + 1] * (i + 1) % M
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(fact[n] * inv_fact[k] % M * inv_fact[n - k] % M)