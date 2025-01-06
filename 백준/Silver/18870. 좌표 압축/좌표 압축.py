input()
x = [*map(int, input().split())]
y = sorted({*x})
y = dict(zip(y, range(len(y))))
print(*[y[i] for i in x])
