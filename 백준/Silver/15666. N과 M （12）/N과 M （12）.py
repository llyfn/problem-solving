I=lambda:map(int,input().split())
_,m=I()
l=sorted({*[*I()]})
n=len(l)
a=[]
def f(i):
    if len(a)==m:print(*a);return
    p=0
    for j in range(i,n):
        if p==l[j]:continue
        a.append(l[j])
        p=l[j]
        f(j)
        a.pop()
f(0)
