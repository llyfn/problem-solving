import itertools as t
I=lambda:map(int,input().split())
n,m=I()
h=[];c=[]
for i in range(n):
    a=[*I()]
    for j in range(n):
        if a[j]>1:c+=(i,j),
        elif a[j]>0:h+=(i,j),
v=1e9
for p in t.combinations(c,m):v=min(v,sum(min(abs(i-x)+abs(j-y)for x,y in p)for i,j in h))
print(v)
