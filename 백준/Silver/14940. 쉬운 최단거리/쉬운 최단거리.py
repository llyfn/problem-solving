I=lambda:map(int,input().split())
n,m=I();g=[]
v=[[0]*m for _ in range(n)]
d=[[-1]*m for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
q=[]
for i in range(n):
    l=[*I()]
    for j in range(m):
        if l[j]>1:v[i][j]=1;d[i][j]=0;q+=(i,j),
        if l[j]<1:d[i][j]=0
    g+=l,
while q:
    x,y=q.pop(0)
    for k in range(4):
        i,j=x+dx[k],y+dy[k]
        if 0<=i<n and 0<=j<m and v[i][j]==0 and g[i][j]==1:v[i][j]=1;d[i][j]=d[x][y]+1;q+=(i,j),
for i in d:print(*i)