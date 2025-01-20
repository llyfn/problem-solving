I=lambda:map(int,input().split())
_,m=I()
l=sorted({*[*I()]})
n=len(l)
a=[]
def f():
    if len(a)==m:print(*a);return
    p=0
    for j in range(n):
        if p==l[j]:continue
        a.append(l[j])
        p=l[j]
        f()
        a.pop()
f()
