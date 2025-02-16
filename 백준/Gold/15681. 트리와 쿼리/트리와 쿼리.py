import sys
sys.setrecursionlimit(10**5)
I=lambda:map(int,sys.stdin.readline().split())
n,r,q=I()
g=[[]for _ in[0]*(n+1)]
for _ in[0]*(n-1):a,b=I();g[a]+=b,;g[b]+=a,
v=[0]*(n+1)
def f(x):
    v[x]=1
    for i in g[x]:
        if v[i]<1:f(i);v[x]+=v[i]
    return v[x]
f(r)
for _ in[0]*q:k,=I();print(v[k])