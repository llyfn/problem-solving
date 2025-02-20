I=lambda:map(int,input().split())
n,=I()
m,d=[[*I()]for _ in[0]*n],[[0]*n for _ in[0]*n]
for i in range(1,n):
    for j in range(n-i):
        d[j][j+i]=1e9
        for k in range(j,j+i):
            d[j][j+i]=min(d[j][j+i],d[j][k]+d[k+1][j+i]+m[j][0]*m[k][1]*m[j+i][1])
print(d[0][n-1])