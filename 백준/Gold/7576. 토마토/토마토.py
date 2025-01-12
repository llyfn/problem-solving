import sys, collections as c
I=lambda:map(int,sys.stdin.readline().split())
m,n=I()
a=[[*I()] for _ in range(n)]
dx,dy=[1,-1,0,0],[0,0,1,-1]
q=c.deque([(i,j) for j in range(n) for i in range(m) if a[j][i]==1])
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<m and 0<=ny<n and a[ny][nx]==0:
            a[ny][nx]=a[y][x]+1
            q += (nx,ny),
if any(any(a[i][j]==0 for j in range(m)) for i in range(n)): print(-1)
else: print(max(map(max,a))-1)
