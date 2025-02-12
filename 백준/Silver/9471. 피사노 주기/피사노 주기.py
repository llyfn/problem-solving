I=lambda:map(int,input().split())
p,=I()
for _ in[0]*p:
    n,m=I()
    a,b=1,1
    for i in range(m*m):
        a,b=b,(a+b)%m
        if a==b==1:print(n,i+1);break