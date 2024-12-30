n, k = [*map(int, input().split())]
v = [int(input()) for _ in range(n)]
d = [0] + [10001] * k
for x in v:
    for i in range(x, k + 1): d[i] = min(d[i], d[i - x] + 1)
print(d[k] if d[k] < 10001 else -1)
