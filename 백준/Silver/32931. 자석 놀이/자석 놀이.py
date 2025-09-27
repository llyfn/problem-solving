n,*l=map(int,open(0).read().split())
a,b=l[0]+max(0,l[n]),l[0]+l[n]
for x,y in zip(l[1:n],l[n+1:]):a,b=x+max(a+max(0,y),b+y),y+max(b+max(0,x),a+x)
print(b)