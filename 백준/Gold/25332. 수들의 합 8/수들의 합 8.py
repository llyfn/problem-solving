n,*l=map(int,open(0).read().split())
d={0:1};r=k=0
for a,b in zip(l,l[n:]):k+=a-b;v=d.get(k,0);r+=v;d[k]=v+1
print(r)