I=lambda:map(int,input().split())
n,s,r=I()
l=[0]*(n+1)
a=set(I())
b=set(I())
for i in a-b:l[i]=1
for i in b-a:
    if i>1==l[i-1]:l[i-1]=0
    elif n>i and l[i+1]:l[i+1]=0
print(sum(l))