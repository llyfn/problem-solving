a,b=map(int,open(0).read().split())
if a%3!=b%3:print(-1)
else:print(a//3,a%3,b//3)