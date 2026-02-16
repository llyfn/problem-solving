from math import *

while True:
    xl, yl, xu, yu, xa, ya, xb, yb = map(int, input().split())
    if not any([xl, yl, xu, yu, xa, ya, xb, yb]): break
    corners = [(xl, yl), (xu, yl), (xl, yu), (xu, yu)]
    def l2(x1, y1, x2, y2): return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
    eps = 1e-9

    def hit(x1, y1, x2, y2):
        if min(x1, x2) >= xu or max(x1, x2) <= xl or min(y1, y2) >= yu or max(y1, y2) <= yl: return False
        dx, dy = x2 - x1, y2 - y1
        if abs(dx) < eps: return xl < x1 < xu
        if abs(dy) < eps: return yl < y1 < yu
        t_s, t_e = 0.0, 1.0
        for p, q in (-dx, x1 - xl), (dx, xu - x1), (-dy, y1 - yl), (dy, yu - y1):
            if abs(p) < eps:
                if q < 0: return False
            else:
                t = q / p
                if p < 0:
                    if t > t_e: return False
                    t_s = max(t_s, t)
                else:
                    if t < t_s: return False
                    t_e = min(t_e, t)
        return t_s < t_e - eps

    def solve(x1, y1, x2, y2):
        res = 1e9

        if not hit(x1, y1, x2, y2): res = l2(x1, y1, x2, y2)

        for cx, cy in corners:
            if not hit(x1, y1, cx, cy) and not hit(cx, cy, x2, y2): res = min(res, l2(x1, y1, cx, cy) + l2(cx, cy, x2, y2))
            for dx, dy in corners:
                if (cx == dx) ^ (cy == dy) and not hit(x1, y1, cx, cy) and not hit(dx, dy, x2, y2):
                    res = min(res, l2(x1, y1, cx, cy) + l2(cx, cy, dx, dy) + l2(dx, dy, x2, y2))

        if (x1 <= xl and x2 >= xu) or (x2 <= xl and x1 >= xu):
            if x1 > x2: x1, y1, x2, y2 = x2, y2, x1, y1
            dx = x2 - x1 - xu + xl
            dy = y2 - y1
            cand = {yl, yu}
            if dx > eps:
                yc = y1 + dy * (xl - x1) / dx
                cand.add(int(floor(yc)))
                cand.add(int(ceil(yc)))
            else: cand.add(int(y1))
            for c in cand:
                if yl <= c <= yu: res = min(res, l2(x1, y1, xl, c) + xu - xl + l2(xu, c, x2, y2))

        if (y1 <= yl and y2 >= yu) or (y2 <= yl and y1 >= yu):
            if y1 > y2: x1, y1, x2, y2 = x2, y2, x1, y1
            dx = x2 - x1
            dy = y2 - y1 - yu + yl
            cand = {xl, xu}
            if dy > eps:
                xc = x1 + dx * (yl - y1) / dy
                cand.add(int(floor(xc)))
                cand.add(int(ceil(xc)))
            else: cand.add(int(x1))
            for c in cand:
                if xl <= c <= xu: res = min(res, l2(x1, y1, c, yl) + yu - yl + l2(c, yu, x2, y2))
        return res

    in_a, in_b = xl <= xa <= xu and yl <= ya <= yu, xl <= xb <= xu and yl <= yb <= yu

    if in_a and in_b: d = abs(xa - xb) + abs(ya - yb)
    elif in_a or in_b:
        if in_b: xa, ya, xb, yb = xb, yb, xa, ya
        d = min(
            xa - xl + solve(xl, ya, xb, yb),
            xu - xa + solve(xu, ya, xb, yb),
            ya - yl + solve(xa, yl, xb, yb),
            yu - ya + solve(xa, yu, xb, yb)
        )
    else: d = solve(xa, ya, xb, yb)

    print(f"{d:.3f}")
