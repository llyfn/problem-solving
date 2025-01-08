import sys
I=lambda:map(int,sys.stdin.readline().split())
n,m=I()
e=[[*I()] for _ in range(m)]
k=[0]*(n+1)
for i in range(1,n+1):
    q=[i];v=[0]*(n+1);v[i]=1
    while q:
        x=q.pop(0)
        for a,b in e:
            if a==x and not v[b]:v[b]=v[x]+1;q+=b,
            elif b==x and not v[a]:v[a]=v[x]+1;q+=a,
    k[i]=sum(v)
print(k.index(min(k[1:])))