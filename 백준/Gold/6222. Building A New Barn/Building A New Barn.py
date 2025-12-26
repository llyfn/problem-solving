I=list(map(int,open(0).read().split()))
N=I[0];Z=I[1:];X=sorted(Z[::2]);Y=sorted(Z[1::2]);C=list(zip(Z[::2],Z[1::2]))
l,r=X[N-1>>1],X[N>>1];b,t=Y[N-1>>1],Y[N>>1]
k=sum(l<=x<=r and b<=y<=t for x,y in C)
a=(r-l+1)*(t-b+1)-k
f=lambda x,y:sum(abs(u-x)+abs(v-y)for u,v in C)
if a:print(f(l,b),a)
else:v=[f(l+i,b+j)for i,j in((0,1),(0,-1),(1,0),(-1,0))];m=min(v);print(m,v.count(m))