from bisect import*
n,*s=map(int,open(0).read().split())
l=[*sorted(zip(s[::2],s[1::2]))]
d,a=[],[]
for s,e in l:
    x=bisect_left(a,e)
    if x<len(a):a[x]=e
    else:a+=e,
    d+=[x]
r,q=len(a)-1,[]
for i in range(len(d)-1,-1,-1):
    if d[i]==r:r-=1
    else:q+=[l[i][0]]
print(n-len(a))
print(*q[::-1],sep='\n')