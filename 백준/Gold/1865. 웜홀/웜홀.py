I=lambda:[*map(int,input().split())]
for _ in[0]*I()[0]:
    n,m,w=I();d,s=[0]*(n+1),[I()for _ in[0]*m];s+=[[b,a,c]for a,b,c in s]+[[a,b,-c]for a,b,c in[I()for _ in[0]*w]]
    for _ in[0]*(n-1):
        for a,b,c in s:c+=d[a];d[b]=min(d[b],c)
    for a,b,c in s:
        if d[b]>(c:=c+d[a]):print('YES');break
    else:print('NO')