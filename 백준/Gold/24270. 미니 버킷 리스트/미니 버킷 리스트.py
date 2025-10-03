n,k,*s=map(int,open(0).read().split())
r,a=k-sum(s),1
for i in range(n):a=(r+i+1)*a%(10**9+7)
print(a)