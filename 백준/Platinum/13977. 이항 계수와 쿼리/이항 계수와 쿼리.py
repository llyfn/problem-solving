import sys
input = sys.stdin.readline
m = int(input())
M = 10 ** 9 + 7
N = 4 * 10 ** 6
fact = [1]
for i in range(1, N + 1): fact.append(fact[-1] * i % M)
for _ in range(m):
    n, k = map(int, input().split())
    print(fact[n] * pow(fact[k] * fact[n - k], M - 2, M) % M)