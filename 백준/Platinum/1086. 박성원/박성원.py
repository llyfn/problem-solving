import math
r=range
N,*A,K=map(int,open(0).read().split())
D=[[0]*K for _ in[0]*(1<<N)]
R=[[(i*10**len(str(A[j]))+A[j])%K for i in r(K)]for j in r(N)]
D[0][0]=1
for i in r(1<<N):
    for j in r(N):
        if not i&2**j:
            for k in r(K):D[i|(1<<j)][R[j][k]]+=D[i][k]
P,Q=D[2**N-1][0],sum(D[2**N-1])
G=math.gcd(P,Q)
print(f"{P//G}/{Q//G}")