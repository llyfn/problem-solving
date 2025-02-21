I=lambda:map(int,input().split())
n,m=I()
g,p,r=[[*I()]for _ in[0]*m],[*range(n+1)],0
def f(x):
    if p[x]!=x:p[x]=f(p[x])
    return p[x]
for i in range(m):
    a,b=g[i]
    if (x:=f(a))!=(y:=f(b)):
        if x>y:p[x]=y
        else:p[y]=x
    else:r=i+1;break
print(r)