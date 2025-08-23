n,m=map(int,input().split())
print(1+(n<=m)+(n>1)*((n//2<=m)+(-~n//2<=m))+(n>2)*sum(m>=i+(n+2)//3for i in[0,n,n//2,-~n//2]))