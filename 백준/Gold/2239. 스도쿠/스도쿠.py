I=lambda:[*map(int,input())]
s,z=[],[]
for i in range(9):
    s+=(a:=I()),
    for j in range(9):
        if not a[j]:z+=(i,j),
def f(x,y,v):
    for i in range(9):
        if s[x][i]==v or s[i][y]==v:return 0
    for i in range(3):
        for j in range(3):
            if s[i+x//3*3][j+y//3*3]==v:return 0
    return 1
def g(x):
    if x==len(z):
        for i in s:print(''.join(map(str,i)))
        exit()
    m,n=z[x]
    for i in range(1,10):
        if f(m,n,i):
            s[m][n]=i
            g(x+1)
            s[m][n]=0
g(0)