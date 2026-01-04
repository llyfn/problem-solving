from heapq import*
*z,=map(int,open(0).read().split())
n,m,t=z[:3]
G=[[]for _ in range(n+1)]
for u,v,l,x,y in zip(*[iter(z[3:])]*5):G[u]+=(v,l,x,y),;G[v]+=(u,l,x,y),
q=[(0,1)]
S=[1]*(n+1)
while q:
 c,u=heappop(q)
 if u==n:print(c);break
 if S[u]:
  S[u]=0
  for b,l,x,y in G[u]:k=(t-c)*(t>c);heappush(q,(min(c+l/x,c+k+(l-k*x)/y),b))