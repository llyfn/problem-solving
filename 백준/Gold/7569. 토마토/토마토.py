import sys, collections as c
I=lambda:map(int,sys.stdin.readline().split())
m,n,h=I()
a=[[[*I()] for _ in range(n)] for _ in range(h)]
dx,dy,dz=[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]
q=c.deque([(i,j,k) for k in range(h) for j in range(n) for i in range(m) if a[k][j][i]==1])
while q:
    x,y,z=q.popleft()
    for i in range(6):
        nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
        if 0<=nx<m and 0<=ny<n and 0<=nz<h and a[nz][ny][nx]==0:
            a[nz][ny][nx]=a[z][y][x]+1
            q += (nx,ny,nz),
if any(any(any(a[i][j][k]==0 for k in range(m)) for j in range(n)) for i in range(h)): print(-1)
else: print(max(max(max(a[i][j]) for j in range(n)) for i in range(h))-1)
