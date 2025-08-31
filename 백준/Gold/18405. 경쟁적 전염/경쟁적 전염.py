n,k,*m,s,x,y=map(int,open(0).read().split())
t=min((abs(k//n-x+1)+abs(k%n-y+1),m[k])for k in range(n*n)if m[k])
print(t[1]*(t[0]<=s))