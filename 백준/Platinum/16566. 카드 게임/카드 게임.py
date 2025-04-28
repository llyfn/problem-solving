import bisect as b
N,M,K,*S=map(int,open(0).read().split())
C=sorted(S[:M])
p=[*range(M+1)]
def f(x):
    if p[x]!=x:p[x]=f(p[x])
    return p[x]
for k in S[M:]:
    i=f(b.bisect(C,k))
    print(C[i])
    if f(i)!=f(i+1):p[f(i)]=f(i+1)