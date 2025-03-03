l=[*map(int,input().split())]
n=len(l)
d=[[[4*n]*5for _ in[0]*5]for _ in[0]*n]
d[0][0][0]=0
f=lambda a,b:2*(a<1)or[1,3,4,3][a-b]
for i in range(n-1):
    x=l[i]
    for j in range(5):
        for k in range(5):d[i+1][j][x]=min(d[i+1][j][x],d[i][j][k]+f(k,x));d[i+1][x][k]=min(d[i+1][x][k],d[i][j][k]+f(j,x))
print(min(map(min,d[-1])))