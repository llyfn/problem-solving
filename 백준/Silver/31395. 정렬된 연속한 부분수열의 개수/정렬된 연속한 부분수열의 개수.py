n,*s=map(int,open(0).read().split())
l=r=a=0
while r<n-1:
    r+=1
    a+=r-l
    if s[r]<=s[r-1]:l=r
print(a+r-l+1)