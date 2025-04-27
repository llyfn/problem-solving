v=[[r>>i&1for i in range(8)]for r in[6,13,27,54,172,88,160,80]]
m=lambda a,b:[[sum(a[i][k]*b[k][j]for k in range(8))%(10**9+7)for j in range(8)]for i in range(8)]
d=int(input())
r=ans=[[i==j for j in range(8)]for i in range(8)]
while d:d&1and(r:=m(r,v));v=m(v,v);d>>=1
print(r[0][0])