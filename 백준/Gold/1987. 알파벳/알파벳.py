r,c=map(int,input().split())
a=[input()for _ in range(r)]
v=[0]*26
d=[(0,1),(1,0),(0,-1),(-1,0)]
m=0
def f(x,y,n):
    global m;m=max(m,n)
    for i,j in d:
        if 0<=x+i<r and 0<=y+j<c and v[k:=(ord(a[x+i][y+j])-65)]<1:
            v[k]=1;f(x+i,y+j,n+1);v[k]=0
v[ord(a[0][0])-65]=1;f(0,0,1)
print(m)