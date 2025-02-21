import sys
I=lambda:map(int,sys.stdin.readline().split())
R=range
n,=I()
a=[*I()]
m,=I()
d=[[i==j for j in R(n+1)] for i in R(n+1)]
for i in R(1,n):d[i][i+1]=a[i]==a[i-1]
for i in R(n,0,-1):
    for j in R(i+2,n+1):d[i][j]=d[i+1][j-1]&(a[i-1]==a[j-1])
for i in R(m):l,r=I();print(+d[l][r])