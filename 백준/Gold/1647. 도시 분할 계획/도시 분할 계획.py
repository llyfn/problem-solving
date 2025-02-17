I=lambda:map(int,input().split())
n,m=I()
p,g,r,t=[*range(n+1)],[],0,0
for _ in[0]*m:a,b,c=I();g+=[(c,a,b)]
g.sort()
def f(x):
    if p[x]!=x:p[x]=f(p[x])
    return p[x]
for c,a,b in g:
    if (x:=f(a))!=(y:=f(b)):
        if x>y:p[x]=y
        else:p[y]=x
        r+=(t:=c)
print(r-t)