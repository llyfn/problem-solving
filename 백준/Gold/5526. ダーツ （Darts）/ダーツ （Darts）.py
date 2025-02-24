m,*p=[int(s.split()[-1])for s in open(0)]+[0]
l=sorted({i+j for i in p for j in p if i+j<=m})
s,e=0,len(l)
M=l[-1]
while s<e:
    v=l[s]+l[e-1]
    if v>m:v=0;e-=1
    elif v<M:s+=1
    else:M=v;s+=1
print(M)