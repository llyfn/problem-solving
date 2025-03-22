I=lambda:[*map(int,input().split())]
N,M,K=I()
C=[0]+I()
F=[[]for _ in[0]*(N+1)]
V=[0]*(N+1)
for _ in[0]*M:a,b=I();F[a]+=[b];F[b]+=[a]
def f(n):
    f,c,q=1,C[n],[n]
    V[n]=1
    while q:
        n=q.pop(0)
        for i in F[n]:
            if V[i]==0:V[i]=1;q+=[i];f+=1;c+=C[i]
    return f,c
G=[f(i)for i in range(1,N+1)if V[i]==0]
d=[0]*(K+1)
for i in range(len(G)):
    f,c=G[i]
    for j in range(K,f-1,-1):d[j]=max(d[j],d[j-f]+c)
print(d[-2])