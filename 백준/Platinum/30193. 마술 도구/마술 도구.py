n=int(input())
k=(n-1).bit_length()
r=n%2
c=[0]*r+[v for i in range(r,n//2+r)for v in(i,i^2**k-1)]
print(k)
print(n//2)
for j in range(k):print(*(i for i,v in enumerate(c)if v>>j&1))