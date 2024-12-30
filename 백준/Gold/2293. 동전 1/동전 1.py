n, k = [*map(int, input().split())]
v = [int(input()) for _ in range(n)]
d = [1] + [0] * k
for x in v:
    for i in range(x, k + 1): d[i] += d[i - x]
print(d[-1])
