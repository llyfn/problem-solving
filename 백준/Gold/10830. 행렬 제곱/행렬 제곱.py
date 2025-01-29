I=lambda:map(int,input().split())
n,k=I()
l=[[*I()]for _ in range(n)]
def m(a,b):return[[sum(a[i][k]*b[k][j] for k in range(n))%1000 for j in range(n)]for i in range(n)]
def p(b,e):
    x=[[+(i==j) for j in range(n)]for i in range(n)]
    while e:
        if e&1:x=m(x,b)
        b=m(b,b);e>>=1
    return x
r=p(l,k)
for i in r:print(*i)