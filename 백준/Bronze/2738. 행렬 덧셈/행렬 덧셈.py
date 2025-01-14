I=lambda:map(int,input().split())
n,m=I()
a=[[*I()]for _ in range(n)]
b=[[*I()]for _ in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j]+=b[i][j]
for i in a:print(*i)