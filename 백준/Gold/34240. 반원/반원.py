[n], *p, [xa, ya, xb, yb] = [[*map(int, i.split())] for i in open(0)]
l2 = lambda xi, yi, xj, yj: ((xi - xj) ** 2 + (yi - yj) ** 2) ** .5
r = l2(xa, ya, xb, yb)
ux, uy = xb - xa, yb - ya
xc, yc = 2 * xa - xb, 2 * ya - yb
ans = 0
for (x, y) in p:
    dx, dy = x - xa, y - ya
    cp = ux * dy - uy * dx
    if cp >= 0: ans += max(0, l2(xa, ya, x, y) - r)
    else:
        if abs(ux * dx + uy * dy) > r * r: ans += min(l2(xb, yb, x, y), l2(xc, yc, x, y))
        else: ans += -cp / r
print(ans)