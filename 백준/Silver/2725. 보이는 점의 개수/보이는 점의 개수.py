m,r=1001,range
p=[*r(m)]
for i in r(2,m):
 if p[i]==i:
  for k in r(i,m,i):p[k]=p[k]//i*(i-1)
for s in[*open(0)][1:]:print(sum(p[1:int(s)+1])*2+1)