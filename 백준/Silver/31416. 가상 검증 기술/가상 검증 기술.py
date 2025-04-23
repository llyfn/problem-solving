I=lambda:map(int,input().split())
n,=I()
for _ in[0]*n:
    a,b,c,d=I()
    print(min(max(a*i,a*(c-i)+b*d)for i in range(c+1)))