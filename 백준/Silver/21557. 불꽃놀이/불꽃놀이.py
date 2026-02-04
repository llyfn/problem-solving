n,*a=map(int,open(0).read().split())
s,e=sorted([a[0],a[-1]])
print(e-n+2if e-s>n-2 else s-(n-e+s-1)//2if e>n-2else 1)
