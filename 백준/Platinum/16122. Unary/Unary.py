M=998244353
n,m=map(int,input().split())
q,l,r=[1]*(n+1),[0]*(n+1),[0]*(n+1)
for i in range(1,n+1):q[i]=q[i-1]*i%M
for i in range(1,n+1):l[i]=min(-l[i-1]-1,-r[i-1]-1);r[i]=max(-l[i-1],-r[i-1])
if l[-1]<=m<=r[-1]:m-=l[-1];print(q[n]*pow(q[m]*q[n-m],-1,M)%M)
else:print(0)