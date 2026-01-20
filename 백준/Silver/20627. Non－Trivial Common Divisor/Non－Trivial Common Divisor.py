_,*a=map(int,open(0))
s={}
for i in a:
 t=i;d=2;f=set()
 while d*d<=t:
  if t%d<1:
   f.add(d)
   while t%d<1:t//=d
  d+=1
 if t>1:f.add(t)
 for d in f:s[d]=s.get(d,0)+i
print(max(s.values())if s else 0)