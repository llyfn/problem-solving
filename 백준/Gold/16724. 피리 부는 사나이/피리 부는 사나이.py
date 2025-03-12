n,m=map(int,input().split())
a=[input()for _ in[0]*n]
def d(x,y):k,l=[(0,1),(0,-1),(1,0),(-1,0)][['R','L','D','U'].index(a[x][y])];return x+k,y+l
v=[[0]*m for _ in[0]*n]
Z=R=0
def f(x,y,z):
    if v[x][y]>0:
        if v[x][y]==z:global R;R+=1
        return
    v[x][y]=z;f(*d(x,y),z)
for i in range(n):
    for j in range(m):f(i,j,Z:=Z+1)
print(R)