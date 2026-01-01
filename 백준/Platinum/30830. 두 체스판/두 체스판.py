N,*I=map(int,open(0).read().split())
D=[[]for _ in[0]*2*N]
for j in range(2*N):u,v=I[2*j]-1,I[2*j+1]+N-1;t=j<N;D[u]+=(v,t),;D[v]+=(u,t),
if any(len(x)!=2for x in D):print(-1);exit()
a=0
for i in range(2*N):
 if D[i]:
  k=[0,0];u=i;p=0;l=0
  while D[u]:v,t=D[u].pop();D[v].remove((u,t));k[p]+=t;p^=1;u=v;l+=1
  a+=l//2-max(k)
print(a)