import sys
I = lambda: [*map(int, sys.stdin.readline().split())]
n, m = I(); l = I(); s, e = 1, max(l)
while s <= e:
    md = (s + e) >> 1
    if sum([x - md for x in l if x > md]) >= m: s = md + 1
    else: e = md - 1
print(e)