[n,m],*p=[map(int,s.split())for s in open(0)]
r=[*range(1,n+1)]
for a,b in p:r[a-1],r[b-1]=r[b-1],r[a-1]
print(*r)