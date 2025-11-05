N,K,*a=map(int,open(0).read().split())
P=[0]
for i in a:P+=P[-1]+i,
d=[[9**9]*(K+2)for _ in ' '*-~N]
m=d[0][0]=0
for i in range(N):m=max(m,a[i]);d[i+1][1]=-~i*m-P[i+1]
for k in range(K):
 for i in range(1,N+1):
  m=0
  for j in range(i-1,k,-1):m=max(m, a[j]);d[i][k+2]=min(d[i][k+2], d[j][k+1]+(i-j)*m-P[i]+P[j])
print(d[N][-1])