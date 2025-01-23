import heapq as h
I=lambda:map(int,input().split())
n,e=I()
k,=I()
g=[[] for _ in range(n+1)]
for _ in range(e):a,b,c=I();g[a]+=(b,c),
d=[1e9]*(n+1)
d[k]=0
q=[(0,k)]
while q:
    w,v=h.heappop(q)
    if d[v]<w:continue
    for u,c in g[v]:
        if d[u]>w+c:d[u]=w+c;h.heappush(q,(w+c,u))
for i in d[1:]:print(i if i<1e9 else 'INF')