I=lambda:[*map(int,input().split())]
n,e=I()
g={}
for _ in range(e):
    a,b,c=I()
    g[a]=g.get(a,[])+[(b,c)]
    g[b]=g.get(b,[])+[(a,c)]
v,w=I()
def f(s,e):
    d=[1e9]*(n+1)
    d[s]=0;q=[s]
    while q:
        a=q.pop(0)
        for b,c in g.get(a,[]):
            if d[b]>d[a]+c:
                d[b]=d[a]+c
                q+=[b]
    if d[e]==1e9:print(-1);exit()
    return d[e]
print(min(f(1,v)+f(v,w)+f(w,n),f(1,w)+f(w,v)+f(v,n)))