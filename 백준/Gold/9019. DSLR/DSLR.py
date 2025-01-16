import sys, collections as c
I=lambda:map(int,sys.stdin.readline().split())
N=10000;M=1000
for _ in range(next(I())):
    n,m=I()
    v=[0]*N
    q=c.deque([(n,'')])
    while q:
        x,o=q.popleft()
        if x==m:print(o);break
        if v[x]:continue
        v[x]=1
        if v[d:=x*2%N]<1:q+=(d,o+'D'),
        if v[s:=(x-1)%N]<1:q+=(s,o+'S'),
        if v[l:=x%M*10+x//M]<1:q+=(l,o+'L'),
        if v[r:=x//10+x%10*M]<1:q+=(r,o+'R'),
