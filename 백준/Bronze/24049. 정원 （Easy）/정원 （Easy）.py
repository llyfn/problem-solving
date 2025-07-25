I=lambda:[*map(int,input().split())]
n,m=I()
l=I()
u=I()
g=[[0]*m for _ in[0]*n]
g[0][0]=l[0]!=u[0]
for i in range(1,n):g[i][0]=g[i-1][0]!=l[i]
for j in range(1,m):g[0][j]=g[0][j-1]!=u[j]
for i in range(2,n+m-1):
    for j in range(1,i):
        if j<n and i-j<m:g[j][i-j]=g[j-1][i-j]!=g[j][i-j-1]
print(+g[n-1][m-1])