import collections as c
R=range
N,M=map(int,input().split())
a=[[*map(int,input())]for _ in R(N)]
d=[(0,1),(1,0),(0,-1),(-1,0)]
v=[[0]*M for _ in R(N)]
b={}
Z=0
for i in R(N):
    for j in R(M):
        if a[i][j]<1 and v[i][j]<1:
            Z+=1
            v[i][j]=Z;b[Z]=1
            q=c.deque([(i,j)])
            while q:
                x,y=q.popleft()
                for X,Y in d:
                    s,t=x+X,y+Y
                    if 0<=s<N and 0<=t<M and a[s][t]<1 and v[s][t]<1:
                        v[s][t]=Z;b[Z]+=1;q.append((s,t))
for i in R(N):
    for j in R(M):
        if a[i][j]>0:
            k=set()
            for x,y in d:
                s=i+x;t=j+y
                if 0<=s<N and 0<=t<M and a[s][t]<1:k.add(v[s][t])
            a[i][j]=(sum(b.get(x,0)for x in k)+1)%10
for i in a:print(''.join(map(str,i)))