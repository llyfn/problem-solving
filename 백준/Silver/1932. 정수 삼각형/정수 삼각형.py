import sys
I=lambda:map(int,sys.stdin.readline().split())
n,=I()
d=[[*I()]]
for i in range(1,n):
    a=[*I()];b=[0]*len(a)
    for j in range(i):
        b[j]=max(b[j],d[-1][j]+a[j])
        b[j+1]=max(b[j+1],d[-1][j]+a[j+1])
    d+=b,
print(max(d[-1]))
