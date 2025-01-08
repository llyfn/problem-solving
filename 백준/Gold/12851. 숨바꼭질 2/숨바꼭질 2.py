n,k=map(int,input().split())
m=1<<17
v=[0]*m
q=[n]
a=b=0
while q:
    x=q.pop(0)
    if a and v[x]>a:break
    if x==k:a=v[x];b+=1;continue
    for i in (x-1,x+1,2*x):
        if 0<=i<m and v[i] in (0,v[x]+1):v[i]=v[x]+1;q+=i,
print(a,b,sep='\n')