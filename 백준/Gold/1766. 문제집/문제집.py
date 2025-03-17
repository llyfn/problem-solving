import heapq as h
I=lambda:map(int,input().split())
n,m=I()
g=[[]for _ in[0]*(n+1)]
d=[0]*(n+1)
for _ in[0]*m:a,b=I();g[a]+=[b];d[b]+=1
q=[i for i in range(1,n+1)if d[i]<1]
while q:
    x=h.heappop(q)
    print(x,end=' ')
    for y in g[x]:
        d[y]-=1
        if d[y]<1:h.heappush(q,y)