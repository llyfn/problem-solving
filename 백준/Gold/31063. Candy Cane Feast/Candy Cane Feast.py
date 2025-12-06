n,m,*d=map(int,open(0).read().split())
c=d[:n]
for h in d[n:]:
 b=0
 for i in range(n):
  if c[i]>b:
   t=min(c[i],h)
   c[i]+=t-b
   b=t
   if b==h:break
print(*c,sep='\n')