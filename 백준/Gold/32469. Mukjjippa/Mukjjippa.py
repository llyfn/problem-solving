[n],*l=[[*map(int,i.split())]for i in open(0)]
M=998244353
N=1
A=B=W=0
for(r,s,p),(x,y,z)in zip(l[:n],l[n:]):a,b,d=[t*pow((r+s+p)*(x+y+z),-1,M)%M for t in(r*y+s*z+p*x,r*z+s*x+p*y,r*x+s*y+p*z)];S,W=(N+A+B)%M,(W+A*d)%M;N,A,B=N*d%M,S*a%M,S*b%M
print(W)