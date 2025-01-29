I=lambda:map(int,input().split())
M=1<<30
n,=I()
d=[[M*(i!=j)for j in range(n)]for i in range(n)]
for _ in[0]*next(I()):s,e,c=I();d[s-1][e-1]=min(d[s-1][e-1],c)
for i in range(n):
 for j in range(n):
  for k in range(n):d[j][k]=min(d[j][k],d[j][i]+d[i][k])
for i in range(n):
 for j in range(n):print(d[i][j]*(d[i][j]<M),end=' ')
 print()
