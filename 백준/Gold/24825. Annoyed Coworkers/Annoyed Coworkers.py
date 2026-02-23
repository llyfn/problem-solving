[h, c], *s = [[*map(int, i.split())] for i in open(0)]
l = max(i[0] for i in s)
r = l + h * max(i[1] for i in s)
while l < r:
    m = (l + r) // 2
    if sum((m - a) // d for a, d in s) >= h: r = m
    else: l = m + 1
print(l)