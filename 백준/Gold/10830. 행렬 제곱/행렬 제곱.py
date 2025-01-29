I=lambda:map(int,input().split())
n,e=I()
l=[[*I()]for _ in range(n)]
def m(a,b):return[[sum(a[i][k]*b[k][j] for k in range(n))%1000 for j in range(n)]for i in range(n)]
x=[[i==j for j in range(n)]for i in range(n)]
while e:
    if e&1:x=m(x,l)
    l=m(l,l);e>>=1
for i in x:print(*i)