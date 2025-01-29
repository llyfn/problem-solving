I=lambda:map(int,input().split())
n,=I()
a,D,d=[*I()],[1]*n,[1]*n
for i in range(1,n):D[i],d[n-i-1]=max((D[j]+1for j in range(i)if a[i]>a[j]),default=1),max((d[n-j-1]+1for j in range(i)if a[n-i-1]>a[n-j-1]),default=1)
print(max(D[i]+d[i]-1for i in range(n)))
