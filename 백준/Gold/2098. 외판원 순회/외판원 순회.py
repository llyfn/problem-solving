I=lambda:[*map(int,input().split())]
n,=I()
w=[I()for _ in[0]*n]
d=[[0]*(1<<n)for _ in[0]*n]
def f(x,y):
    if y==(1<<n)-1:return w[x][0]or 1e9
    if d[x][y]:return d[x][y]
    d[x][y]=min([1e9]+[f(i,y|(1<<i))+w[x][i]for i in range(1,n)if y&(1<<i)<1and w[x][i]])
    return d[x][y]
print(f(0,1))