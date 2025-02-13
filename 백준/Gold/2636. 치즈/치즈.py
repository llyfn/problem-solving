from collections import deque as q
I=lambda:map(int,input().split())
n,m=I()
a=[[*I()] for _ in range(n)]
d=[(0,1),(1,0),(0,-1),(-1,0)]
r=0
while 1:
    Q=q([(0,0)])
    v=[[0]*m for _ in range(n)]
    v[0][0]=1
    r+=1
    while Q:
        x,y=Q.popleft()
        for dx,dy in d:
            s,t=x+dx,y+dy
            if s<0 or s>=n or t<0 or t>=m:continue
            if a[s][t]:v[s][t]+=1
            elif not v[s][t]:v[s][t]=1;Q.append((s,t))
    k,l=0,0
    for i in range(n):
        for j in range(m):
            if a[i][j]:
                if v[i][j]>0:a[i][j]=0;k+=1
                else:l+=1
    if l==0:break
print(r)
print(k)