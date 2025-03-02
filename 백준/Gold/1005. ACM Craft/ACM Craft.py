I=lambda:[*map(int,input().split())]
for _ in[0]*int(input()):
    n,k=I()
    D=[0]+I()
    p=[[]for _ in[0]*(n+1)]
    o=[0]*(n+1)
    d=[0]*(n+1)
    for _ in[0]*k:
        x,y=I()
        p[x]+=y,
        o[y]+=1
    q=[]
    for i in range(1,n+1):
        if o[i]<1:q+=i,;d[i]=D[i]
    while q:
        x=q.pop(0)
        for y in p[x]:
            o[y]-=1
            d[y]=max(d[y],d[x]+D[y])
            if o[y]<1:q+=y,
    print(d[I()[0]])