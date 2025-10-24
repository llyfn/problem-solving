n,m=map(int,input().split())
a,b=input(),input()
d=[[1e9]*-~m for i in[0]*-~n]
d[0][0]=0
for i in range(n):
    for j in range(m):d[i+1][j+1]=min(d[i][j],d[i+1][j],d[i][j+1])+abs(ord(a[i])-ord(b[j]))
print(d[n][m])