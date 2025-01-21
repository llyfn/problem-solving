import math,heapq as h
I=lambda:map(int,input().split())
n,=I();m,=I()
g=[[]for _ in range(n+1)]
for _ in range(m):s,e,c=I();g[s]+=[(c,e)];g[e]+=[(c,e)]
a,b=I()
d=[math.inf]*(n+1)
d[a]=0;q=[(0,a)]
while q:
    c,e=h.heappop(q)
    if d[e]<c:continue
    for i,j in g[e]:
        if d[j]>c+i:d[j]=c+i;h.heappush(q,(c+i,j))
print(d[b])