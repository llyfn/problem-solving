I=lambda:map(int,input().split())
n,=I()
g=[[]for _ in [0]*(n+1)]
for _ in range(n-1):a,b,c=I();g[a]+=(b,c),;g[b]+=(a,c),
def f(s):
    v=[0]*(n+1);d=v[:];q=[(s,0)]
    while q:
        s,c=q.pop();v[s]=1;d[s]=c
        for i,j in g[s]:
            if v[i]<1:q+=[(i,c+j)]
    return d
print(max(f(f(1).index(max(f(1))))))
