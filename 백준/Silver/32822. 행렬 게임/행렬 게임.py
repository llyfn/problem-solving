I=lambda:[*map(int,input().split())]
n,m=I()
a=[I()for _ in[0]*n]
b=[I()for _ in[0]*n]
d=[max(abs(a[i][j]-b[i][j])for i in range(n))for j in range(n)]
print(sum(d[i-1]for i in I()))