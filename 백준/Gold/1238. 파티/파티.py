import heapq as h
P,S=h.heappop,h.heappush
I=lambda:map(int,input().split())
n,m,x=I()
g=[[] for _ in range(n+1)]
for i in range(m):a,b,c=I();g[a]+=[(b,c)]
def f(s):
    d=[0]+[1e9]*n
    d[s]=0
    q=[(0,s)]
    while q:
        c,v=P(q)
        if d[v]<c:continue
        for u,w in g[v]:
            if d[u]>c+w:d[u]=c+w;S(q,(c+w,u))
    return d
r=f(x)
for i in range(1,n+1):r[i]+=f(i)[x]
print(max(r))