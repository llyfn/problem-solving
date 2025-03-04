n=int(input())
if n==1:print(0);exit()
p=[1]*(n+1)
p[0]=p[1]=0
for i in range(2,int(n**.5)+1):
    if p[i]:
        for j in range(2*i,n+1,i):p[j]=0
P=[i for i in range(n+1)if p[i]]
r=0
i=j=len(P)-1
a=P[-1]
while 0<=i<=j<len(P):
    if a>n:a-=P[j];j-=1
    else:
        r+=a==n;i-=1
        if i<0:break
        a+=P[i]
print(r)