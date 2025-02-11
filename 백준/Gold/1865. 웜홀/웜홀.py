I=lambda:[*map(int,input().split())]
for _ in[0]*I()[0]:
    n,m,w=I();s,d=[[]for _ in range(n+1)],[1e9]*(n+1);d[1]=0
    for _ in[0]*m:a,b,c=I();s[a]+=(b,c),;s[b]+=(a,c),
    for _ in[0]*w:a,b,c=I();s[a]+=(b,-c),
    for _ in[0]*n:
        for i in range(1,n+1):
            for j,k in s[i]:d[j]=min(d[j],d[i]+k)
    for i in range(1,n+1):
        for j,k in s[i]:
            if d[j]>d[i]+k:print('YES');break
        else:continue
        break
    else:print('NO')