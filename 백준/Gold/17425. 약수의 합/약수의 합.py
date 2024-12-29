n = int(input())
a = [int(input()) for _ in range(n)]
max_n = 1000001
g = [1] * max_n

for i in range(2, max_n):
    for j in range(i, max_n, i):
        g[j] += i
    g[i] += g[i - 1]

for i in a:
    print(g[i])
