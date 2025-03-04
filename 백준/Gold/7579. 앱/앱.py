I=lambda:[*map(int,input().split())]
n,m=I()
a=[0]+I()
c=[0]+I()
d=[[0]*(sum(c)+1)for _ in[0]*(n+1)]
r=1e9
for i in range(1,n+1):
    for j in range(sum(c)+1):
        d[i][j]=max(d[i][j],d[i-1][j],d[i-1][j-c[i]]+a[i]if j>=c[i]else 0)
        if d[i][j]>=m:r=min(r,j)
print(r)