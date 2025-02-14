I=lambda:map(int,input().split())
n,=I()
m,o,t,f,d=[],2,0,0,[(-1,0),(0,-1),(0,1),(1,0)]
for i in range(n):
    m+=(l:=[*I()]),
    if 9 in l:a,b=i,l.index(9)
while 1:
    q,v,r,m[a][b]=[(a,b)],[[0]*n for _ in range(n)],[],0
    while q:
        x,y=q.pop(0)
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and v[nx][ny]<1 and m[nx][ny]<=o:
                v[nx][ny]=v[x][y]+1;q+=(nx,ny),
                if 0<m[nx][ny]<o:r+=(v[nx][ny],nx,ny),
    if not r:break
    c,a,b=sorted(r).pop(0);t+=c;f+=1
    if f==o:f=0;o+=1
print(t)