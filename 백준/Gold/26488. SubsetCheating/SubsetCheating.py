from math import comb
n, a, b = map(int, input().split())
m = 10**9 + 7
print(0 if a < b else (comb(b + n - 1, n - 1) % m) * (comb((a - b) + n - 1, n - 1) % m) % m)
