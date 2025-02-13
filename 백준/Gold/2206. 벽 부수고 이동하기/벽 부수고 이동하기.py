import collections as c
n,m=map(int,input().split())
a=[input() for _ in range(n)]
d=[(0,1),(1,0),(0,-1),(-1,0)]
q=c.deque([(0,0,1)])
v=[[[0,0]for _ in range(m)]for _ in range(n)]
v[0][0][1]=1
while q:
    x,y,z=q.popleft()
    if x==n-1 and y==m-1:print(v[x][y][z]);break
    for dx,dy in d:
        s,t=x+dx,y+dy
        if s<0 or s>=n or t<0 or t>=m:continue
        if a[s][t]=='1' and v[s][t][0]==0 and z:v[s][t][0]=v[x][y][z]+1;q.append((s,t,0))
        elif a[s][t]=='0' and v[s][t][z]==0:v[s][t][z]=v[x][y][z]+1;q.append((s,t,z))
else:print(-1)