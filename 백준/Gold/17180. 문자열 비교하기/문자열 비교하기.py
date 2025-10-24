n,m=map(int,input().split())
a,b=[[*map(ord,input())]for _ in'  ']
d=[[0]*-~m for i in[0]*-~n]
for i in range(n):d[i+1][1]=d[i][1]+abs(a[i]-b[0])
for i in range(m):d[1][i+1]=d[1][i]+abs(a[0]-b[i])
for i in range(1,n):
    for j in range(1,m):d[i+1][j+1]=min(d[i][j],d[i+1][j],d[i][j+1])+abs(a[i]-b[j])
print(d[n][m])