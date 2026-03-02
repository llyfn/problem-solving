from collections import Counter

input()
arr = [*map(int, input().split())]
cnt = Counter(arr)
vals = list(cnt.keys())
sides = {0: []}
for i in range(len(vals)):
    x = vals[i]
    sides[0].append(x)
    for j in range(i + 1, len(vals)):
        y = vals[j]
        d = abs(x - y)
        if d not in sides: sides[d] = []
        sides[d].append(min(x, y))
ans = 0
for d, s in sides.items():
    if d == 0:
        vs = [x for x in s if cnt[x] > 1]
        for i in range(len(vs)):
            if cnt[vs[i]] >= 6: ans += 1
            for j in range(i + 1, len(vs)):
                ans += (cnt[vs[i]] >= 4) + (cnt[vs[j]] >= 4) + len(vs) - j - 1
    else:
        u = {}
        for x in s: u[x] = min(3, cnt[x], cnt[x + d])
        vs = sorted([x for x in s if u[x]])
        pos = {vs[i]: i for i in range(len(vs))}
        for i in range(len(vs)):
            js = i if u[vs[i]] >= 2 else i + 1
            for j in range(js, len(vs)):
                if vs[j] == vs[i] + d and cnt[vs[j]] < 2: continue
                if vs[i] == vs[j]: ks = j if u[vs[i]] >= 3 else j + 1
                else: ks = j if u[vs[j]] >= 2 else j + 1
                if ks >= len(vs): continue
                ans += (len(vs) - ks)
                if vs[i] + d in pos:
                    if pos[vs[i] + d] >= ks and cnt[vs[i] + d] < 2 + (vs[i] + d in [vs[j], vs[j] + d]): ans -= 1
                if vs[j] + d != vs[i] + d and vs[j] + d in pos:
                    if pos[vs[j] + d] >= ks and cnt[vs[j] + d] < 2: ans -= 1
print(ans)