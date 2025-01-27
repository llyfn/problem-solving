n=int(input())
s='*';r=2*2**n-3;c=2**n-1
m=[[' ']*r for _ in range(c)]
def f(x,y,z):
    if z<2:m[y][x]=s;return
    k=2*2**z-3;l=2**z-1
    if z&1:
        for i in range(x,k+x):m[y+l-1][i]=s
        for i in range(l):m[y+i][x+k//2-i]=m[y+i][x+k//2+i]=s
    else:
        for i in range(x,k+x):m[y][i]=s
        for i in range(1,l):m[y+i][x+i]=m[y+i][x+k-i-1] = s
    f(x+2**z//2,y+(l//2 if z&1 else 1),z-1)
f(0,0,n)
for i in range(c):
    for j in range(r-c+i+1 if n&1 else r-i):print(m[i][j],end="")
    print()
