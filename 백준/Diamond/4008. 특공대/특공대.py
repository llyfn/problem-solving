n,a,b,c,*l=map(int,open(0).read().split())
h=[(-9e18,0,0)]
s=p=0
for w in l:
 s+=w
 while p+1<len(h)and h[p+1][0]<=s:p+=1
 if p>99:h=h[p:];p=0
 x,k,m=h[p]
 K=-2*a*s;M=2*a*s*s+c+k*s+m
 while len(h)>1and(h[-1][2]-M)/(K-h[-1][1])<=h[-1][0]:h.pop()
 h+=((h[-1][2]-M)/(K-h[-1][1]),K,M),
print(a*s*s+b*s+c+k*s+m)