_, *l = [[*map(int, i.split())] for i in open(0)]
def f(x, y):
    if x > y: x, y = y, x
    return (x + 1) / 6 * (x * (2 * x + 1) + 3 * y * (y - x + 1))
ans = 0
for (l1, h1), (l2, h2) in zip(l, l[1:]):
    ans += (f(h1, h2) - f(l1 - 1, h2) - f(h1, l2 - 1) + f(l1 - 1, l2 - 1)) / (h1 - l1 + 1) / (h2 - l2 + 1)
print(ans)