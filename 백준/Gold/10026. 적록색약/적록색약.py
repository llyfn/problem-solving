import collections as c
n=int(input())
a=[input() for _ in range(n)]
dx,dy=[1,-1,0,0],[0,0,1,-1]
def f(x,y,s,b):
    q=c.deque([(x,y)])
    v[b][x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and v[b][nx][ny]==0 and (a[nx][ny]==s or b and s in 'RG' and a[nx][ny] in 'RG'):
                v[b][nx][ny]=1
                q+=(nx,ny),
k,l=0,0
v=[[[0]*n for _ in range(n)] for _ in range(2)]
for i in range(n):
    for j in range(n):
        if v[0][i][j]==0: f(i,j,a[i][j],0);k+=1
        if v[1][i][j]==0: f(i,j,a[i][j],1);l+=1
print(k,l)
