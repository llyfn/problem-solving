n, m = map(int, input().split())
b = [[*map(lambda s: 1 if s == 'W' else 0, input())] for _ in range(n)]
r = 64
for i in range(n - 7):
    for j in range(m - 7):
        c = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == b[i + x][j + y]: c += 1
        r = min(r, c, 64 - c)
print(r)