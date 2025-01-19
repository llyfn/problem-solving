import collections as c
n=int(input())
g=dict()
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a]=g.get(a,[])+[b]
    g[b]=g.get(b,[])+[a]
q=c.deque([1])
v=[0]*(n+1)
while q:
    p=q.popleft()
    for i in g[p]:
        if not v[i]:v[i]=p;q.append(i)
print(*v[2:],sep='\n')