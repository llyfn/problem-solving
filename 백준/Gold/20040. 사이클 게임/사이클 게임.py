I=lambda:map(int,input().split())
n,m=I()
p,r=[*range(n+1)],0
def f(x):
    if p[x]-x:p[x]=f(p[x])
    return p[x]
for i in range(m):
    x,y=map(f,I())
    if x-y:
        if x>y:p[x]=y
        else:p[y]=x
    else:r=i+1;break
print(r)