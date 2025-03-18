from bisect import*
a,b,c,d=[],[],[],[]
for s in[*open(0)][1:]:x,y,z,w=map(int,s.split());a+=x,;b+=y,;c+=z,;d+=w,
e,f,g=[],[],0
for i in a:
    for j in b:e+=i+j,
for i in c:
    for j in d:f+=i+j,
e.sort()
f.sort()
l,r=0,len(f)-1
L,R=bisect_left,bisect
while l<len(e) and r>=0:
    t=e[l]+f[r]
    if t>0:r-=1
    elif t<0:l+=1
    else:x,y=R(e,e[l])-L(e,e[l]),R(f,f[r])-L(f,f[r]);g+=x*y;l+=x;r-=y
print(g)