I=lambda:[*map(int,input().split())]
t,=I();n,=I();a=I();m,=I();b=I()
c={}
for i in range(n):
    s=0
    for j in range(i,n):s+=a[j];c[s]=c.get(s,0)+1
print(sum(sum([s:=0,*[c.get(t-(s:=s+b[j]),0)for j in range(i,m)]])for i in range(m)))