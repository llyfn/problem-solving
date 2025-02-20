m=1001
R=range
d=[[0]*m for _ in R(m)]
d[1][1]=d[2][1]=d[3][1]=1
for j in R(2,m):
    for i in R(1,m):
        for k in R(1,min(4,i)):d[i][j]=(d[i-k][j-1]+d[i][j])%(10**9+9)
for i in[*open(0)][1:]:n,m=map(int,i.split());print(d[n][m])