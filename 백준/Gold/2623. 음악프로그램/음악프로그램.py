I=lambda:map(int,input().split())
n,m=I()
a=[[]for _ in[0]*(n+1)]
r=[]
d=[0]*(n+1)
for _ in[0]*m:
    l=[*I()][1:]
    for i in range(len(l)-1):a[l[i]]+=l[i+1],;d[l[i+1]]+=1
q=[i for i in range(1,n+1)if d[i]<1]
while q:
    x=q.pop()
    r+=x,
    for i in a[x]:
        d[i]-=1
        if d[i]<1:q+=[i]
if len(r)<n:print(0)
else:print(*r,sep='\n')