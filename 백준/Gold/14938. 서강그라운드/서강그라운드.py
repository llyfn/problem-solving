I=lambda:map(int,input().split())
n,m,r=I()
t=[0,*I()]
R=range(n+1)
d=[[1e9*(j!=i)for j in R]for i in R]
for i in range(r):a,b,c=I();d[a][b]=d[b][a]=c
for i in R:
    for j in R:
        for k in R:d[j][k]=min(d[j][k],d[j][i]+d[i][k])
print(max(sum(t[j]for j in R if d[j][i]<=m)for i in R))
