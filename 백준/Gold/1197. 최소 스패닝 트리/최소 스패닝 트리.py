import sys
sys.setrecursionlimit(10**5)
I=lambda:map(int,sys.stdin.readline().split())
v,e=I()
p,g,c=[*range(v+1)],[],0
for _ in[0]*e:a,b,w=I();g+=[(w,a,b)]
g.sort()
def f(x):
    if p[x]!=x:p[x]=f(p[x])
    return p[x]
for w,a,b in g:
    if (m:=f(a))!=(n:=f(b)):
        if m<n:p[n]=m
        else:p[m]=n
        c+=w
print(c)