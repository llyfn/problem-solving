import heapq as h
I=lambda:map(int,input().split())
n,=I()
m,=I()
g=[[]for _ in[0]*(n+1)]
for _ in[0]*m:a,b,c=I();g[a]+=(b,c),
s,e=I()
d=[[1e9,[i]]for i in range(n+1)]
d[s][0]=0
q=[(0,s)]
while q:
    c,u=h.heappop(q)
    x,y=d[u]
    if x<c:continue
    for v,w in g[u]:
        if d[v][0]>c+w:d[v]=[c+w,[*y,v]];h.heappush(q,(c+w,v))
x,y=d[e]
print(x)
print(len(y))
print(*y)