N = 5000001; p = [*range(N)]
for i in range(2, 2237):
    if p[i] == i:
        for j in range(i*2, N, i):
            if p[j] == j: p[j] = i
input()
for i in map(int, input().split()):
    f = []
    while i > 1: f += p[i],; i //= p[i]
    print(*f)