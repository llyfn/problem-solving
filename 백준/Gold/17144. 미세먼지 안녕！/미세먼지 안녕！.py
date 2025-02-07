I=lambda:map(int,input().split())
r,c,t=I()
a,w=[],[]
R,C=range(r),range(c)
for i in R:
    a+=(k:=[*I()]),
    if k[0]<0:w+=i,
d=[(0,1),(-1,0),(0,-1),(1,0)],[(0,1),(1,0),(0,-1),(-1,0)]
def f():
    k=[[0]*c for _ in R]
    for i in R:
        for j in C:
            if (v:=a[i][j])>0:
                for dx,dy in d[0]:
                    p,q=i+dx,j+dy
                    if 0<=p<r and 0<=q<c and a[p][q]>-1:k[p][q]+=v//5;k[i][j]-=v//5
    for i in R:
        for j in C:a[i][j]+=k[i][j]
def g(v):
    x,y,z,s=w[v],0,0,0
    while 1:
        dx,dy=d[v][z];p,q=x+dx,y+dy
        if (p,q)==(w[v],0):break
        if p<0 or p>=r or q<0 or q>=c:z+=1;continue
        a[p][q],s=s,a[p][q];x,y=p,q
for _ in range(t):f();g(0);g(1)
print(sum(sum(i)for i in a)+2)