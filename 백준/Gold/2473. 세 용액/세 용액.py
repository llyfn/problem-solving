n,*a=map(int,open(0).read().split())
a.sort()
b=[1e9]*3
for i in range(n):
    l,r=i+1,n-1
    while l<r:
        if abs(s:=a[i]+a[l]+a[r])<abs(sum(b)):b=[a[i],a[l],a[r]]
        l+=s<0;r-=s>=0
print(*b)