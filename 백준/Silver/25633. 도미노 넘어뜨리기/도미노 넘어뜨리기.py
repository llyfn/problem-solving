n,*a=map(int,open(0).read().split())
d=[0]*-~n
for x in a:
    for j in range(n,0,-1):
        if 0<d[j-1]>=x:d[j]=max(d[j],d[j-1]+x)
    d[1]=max(d[1],x)
print(max(i for i,v in enumerate(d)if v))