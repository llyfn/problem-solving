N, a, b = map(int, input().split())
m = 10**9 + 7
def comb(n, r):
    r = min(r, n - r)
    x = y = 1
    for i in range(r):
        x = x * (n - i) % m
        y = y * (i + 1) % m
    return x * pow(y, m - 2, m) % m
print(0 if a < b else comb(N + b - 1, N - 1) * comb(N + a - b - 1, N - 1) % m)
