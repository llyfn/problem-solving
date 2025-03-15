n,m,*l=map(int,open(0).read().split())
for i in range(n-1,-1,-1):
    if(m:=m-l[i])<1:print(i+1);break
else:print(-1)