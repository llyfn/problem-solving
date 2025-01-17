n,m=input().split()
m=int(m+n);n=int(n)
for i in range(2,int(m**0.5)+1):
    if m%i==0 or n%i==0:print('No');break
else:print('Yes')