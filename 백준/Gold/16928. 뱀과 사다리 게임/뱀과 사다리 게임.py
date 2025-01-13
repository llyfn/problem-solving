I=lambda:map(int,input().split())
n,m=I()
l=dict(I() for _ in range(n))
s=dict(I() for _ in range(m))
v=[0]*101
q=[1]
while q:
    x=q.pop(0)
    for i in range(1,7):
        y=x+i
        if y in l:y=l[y]
        if y in s:y=s[y]
        if y==100:print(v[x]+1);break
        if y<100 and not v[y]:v[y]=v[x]+1;q+=y,
    else:continue
    break
