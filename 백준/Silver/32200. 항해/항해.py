n,x,y,*a=map(int,open(0).read().split())
m=t=0
for i in a:m+=i//x;t+=max(0,i-i//x*y)
print(m);print(t)