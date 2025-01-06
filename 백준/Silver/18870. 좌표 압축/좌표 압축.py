n = int(input())
x = map(int, input().split())
y = {}
z = [0] * n
for idx, i in enumerate(x): y.setdefault(i, []).append(idx)
for idx, i in enumerate(sorted(y.items(), key=lambda w: w[0])):
    for j in i[1]: z[j] = idx
print(*z)