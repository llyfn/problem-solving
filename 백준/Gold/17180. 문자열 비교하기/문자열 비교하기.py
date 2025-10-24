n,m=map(int,input().split())
a,b=[[*map(ord,input())]for _ in'  ']
d=[[1e9]*-~m for i in[0]*-~n]
d[0][0]=0
for i in range(n):
    for j in range(m):d[i+1][j+1]=min(d[i][j],d[i+1][j],d[i][j+1])+abs(a[i]-b[j])
print(d[n][m])