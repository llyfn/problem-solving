n,m,*l=map(int,open(0).read().split())
r=0
for k in l[:m]:
    s=0;h={}
    for x,y in zip(l[m::2],l[m+1::2]):c=h.get(i:=y-k*x,0);s+=c+c;h[i]=c+1
    r+=s
print(r)