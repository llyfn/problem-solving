I=lambda:map(int,input().split())
n,m=I()
d=[(0,1),(1,0),(0,-1),(-1,0)]
a=[[*I()]for _ in[0]*n]
r=0
def f(c):
    if c>2:
        b=[i[:]for i in a];q=[]
        for i in range(n):
            for j in range(m):
                if b[i][j]>1:q+=(i,j),
        while q:
            x,y=q.pop(0)
            for i,j in d:
                k,l=x+i,y+j
                if 0<=k<n and 0<=l<m and b[k][l]<1:b[k][l]=2;q+=(k,l),
        global r;r=max(r,sum(i.count(0)for i in b));return
    for i in range(n):
        for j in range(m):
            if a[i][j]<1:a[i][j]=1;f(c+1);a[i][j]=0
f(0)
print(r)
