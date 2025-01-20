I=lambda:map(int,input().split())
n,m=I()
l=sorted([*I()])
v=[0]*n
a=[]
def f(i):
    if len(a)==m:print(*a);return
    p=0
    for j in range(i,n):
        if v[j]or p==l[j]:continue
        v[j]=1
        a.append(l[j])
        p=l[j]
        f(j)
        v[j]=0
        a.pop()
f(0)