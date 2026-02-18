cp = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
while True:
    v1 = *map(int, input().split()),
    if not any(v1): break
    v2 = *map(int, input().split()),
    v3 = *map(int, input().split()),
    w = *map(int, input().split()),
    input()
    det = cp(v1, v2, v3)
    if det:
        c1, c2, c3 = cp(w, v2, v3), cp(w, v3, v1), cp(w, v1, v2)
        print("YES" if det > 0 and c1 > 0 and c2 > 0 and c3 > 0 or det < 0 and c1 < 0 and c2 < 0 and c3 < 0 else "NO")
    else:
        if cp(v1, v2, w) or cp(v1, v3, w): print("NO")
        elif v1 == v2 == v3 == w or min(v1[0], v2[0], v3[0]) < w[0] < max(v1[0], v2[0], v3[0]) or min(v1[1], v2[1], v3[1]) < w[1] < max(v1[1], v2[1], v3[1]): print("YES")
        else: print("NO")
