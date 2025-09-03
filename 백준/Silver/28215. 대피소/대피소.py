from itertools import*
n,k,*l=map(int,open(0).read().split())
r=range(n)
print(min(max(min(abs(l[2*i]-l[2*j])+abs(l[2*i+1]-l[2*j+1])for j in c)for i in r)for c in combinations(r,k)))