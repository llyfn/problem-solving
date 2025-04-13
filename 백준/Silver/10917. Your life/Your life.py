n,m,*l=map(int,open(0).read().split())
g=[[]for _ in[0]*(n+1)]
v=[1]*(n+1)
for i,j in zip(l[::2],l[1::2]):g[i]+=j,
q=[(1,0)]
while q:
    i,j=q.pop(0)
    if i==n:print(j);break
    for k in g[i]:
        if v[k]:q+=(k,j+1),;v[k]=0
else:print(-1)