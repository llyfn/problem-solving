n,r,c=map(int,input().split())
f=lambda x:sum((x>>i&1)*4**i for i in range(n))
print(2*f(r)+f(c))