I=lambda:map(int,input().split())
n,=I()
a=[[*I()]for _ in[0]*n]
R=M=1e9
for i in(0,1,2):
    d=[[M]*3for _ in[0]*n]
    d[0][i]=a[0][i]
    for j in range(1,n):r,g,b=a[j];x,y,z=d[j-1];d[j]=[r+min(y,z),g+min(x,z),b+min(x,y)]
    d[-1][i]=M;R=min(R,*d[-1])
print(R)