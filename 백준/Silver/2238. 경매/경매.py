import collections as c
s=[*open(0)][1:]
g=[i.split() for i in s]
C=c.Counter(x[1]for x in g)
print(*sorted([x for x in g if C[x[1]]<=min(C.values())],key=lambda x:int(x[1]))[0])