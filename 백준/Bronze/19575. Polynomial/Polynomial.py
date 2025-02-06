I=lambda:map(int,input().split())
m=10**9+7
n,x=I()
s=0
for i in range(n,-1,-1):
    a,b=I()
    s+=a*pow(x,b,m)
print(s%m)