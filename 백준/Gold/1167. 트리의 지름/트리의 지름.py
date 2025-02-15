import itertools as t
I=lambda:map(int,input().split())
n,=I()
g=[[]for _ in[0]*(n+1)]
for _ in[0]*n:a,*l,_=I();g[a]+=[(b,c)for b,c in t.batched(l,2)]
def f(s):
    v,q=[0]*(n+1),[(s,0)];d=v[:]
    while q:s,c=q.pop();v[s],d[s]=1,c;q+=[(i,c+j)for i,j in g[s]if v[i]<1]
    return d
print(max(f(f(1).index(max(f(1))))))