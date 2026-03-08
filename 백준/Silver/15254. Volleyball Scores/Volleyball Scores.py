i = iter(open(0).read().split())
k = int(next(i, 0))
for d in range(1, k + 1):
    s = [next(i) for _ in range(int(next(i)))]
    a = b = w = r = 0
    e = None
    for x in s:
        if not r:
            m = 'A' if int(x) < 7 else 'B'
            if e and m != e:
                w = 1; break
            e, c, l, u, f, r = ('B' if m == 'A' else 'A'), m, int(x), 1, 1, 1
        elif x in 'ABX':
            if x == 'A' or (x == 'X' and c == 'A'): b += 1
            else: a += 1
            r = 0
        else:
            p, m = int(x), 'A' if int(x) < 7 else 'B'
            if p == l or (f and m == c) or (m == c and u == 3):
                if m == 'A': b += 1
                else: a += 1
                r = 0
            else:
                u = u + 1 if m == c else 1
                c, l, f = m, p, 0
    print(f"Data Set {d}:\n{'Wrong Serve' if w else f'{a} {b}'}\n")