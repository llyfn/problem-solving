n,*l=map(int,open(0).read().split())
p=[0,*[x-y for x,y in zip(l[:n],l[n:])],0]
print(sum(abs(y-x)for x,y in zip(p,p[1:]))//2)