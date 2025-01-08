n,k=map(int,input().split())
m=1<<17
v=[0]*m
q=[n]
while q:
    x=q.pop(0)
    if x==k:print(v[x]);break
    for i in (x-1,x+1,2*x):
        if 0<=i<m and not v[i]:v[i]=v[x]+1;q+=i,
