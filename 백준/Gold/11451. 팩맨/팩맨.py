from collections import*
d=[(-1,0,'N'),(0,1,'E'),(0,-1,'W'),(1,0,'S')]
for _ in[0]*int(input()):
    m,n=map(int,input().split())
    g=[]
    p=[]
    for i in range(m):
        g+=(s:=input()),
        for j in range(n):
            if s[j]=='P':p+=i,j,
    q=deque([(*p,'')])
    v={(*p,)}
    while q:
        w,x,y,z,s=q.popleft()
        if (w,x)==(y,z):print(len(s),s);break
        for i,j,k in d:
            nw,nx,ny,nz=(w+i)%m,(x+j)%n,(y+i)%m,(z+j)%n
            if g[nw][nx]=='X':nw,nx=w,x
            if g[ny][nz]=='X':ny,nz=y,z
            if g[nw][nx]=='G' or g[ny][nz]=='G' or (nw,nx,ny,nz) in v:continue
            v.add((nw,nx,ny,nz))
            q.append((nw,nx,ny,nz,s+k))
    else:print("IMPOSSIBLE")