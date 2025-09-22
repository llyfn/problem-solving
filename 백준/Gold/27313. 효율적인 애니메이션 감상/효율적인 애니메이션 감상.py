n,m,k,*l=map(int,open(0).read().split())
l.sort()
d=[]
for i in range(n):
    a=l[i]if i<k else d[i-k]+l[i]
    if a>m:break
    d+=a,
print(len(d))