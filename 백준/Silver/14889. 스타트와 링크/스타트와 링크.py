from itertools import*
[n],*s=[[*map(int,i.split())]for i in open(0)]
r=range(n)
m=10**9
for t in combinations(r,n//2):c=set(r)-set(t);m=min(abs(sum(s[i][j]for i in t for j in t)-sum(s[i][j]for i in c for j in c)),m)
print(m)