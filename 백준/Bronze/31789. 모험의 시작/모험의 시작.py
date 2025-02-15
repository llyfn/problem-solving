I=lambda:map(int,input().split())
n,=I()
x,s=I()
for i in[0]*n:
    c,p=I()
    if x>=c and s<p:print('YES');break
else:print('NO')