I=lambda:map(int,input().split())
for _ in range(next(I())):
    n,=I()
    a=[*I()];b=[*I()]
    d=[[0]*2]*2
    for i in range(n):d+=[a[i]+max(d[i+1][1],max(d[i])),b[i]+max(d[i+1][0],max(d[i]))],
    print(max(d[-1]))
