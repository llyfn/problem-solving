import collections as C
s = sorted([int(input()) for i in range(int(input()))])
print(round(sum(s) / len(s)))
print(s[len(s) // 2])
c = C.Counter(s)
print((l := sorted([i for i, j in c.items() if j == max(c.values())]))[1 if len(l) > 1 else 0])
print(s[-1] - s[0])
