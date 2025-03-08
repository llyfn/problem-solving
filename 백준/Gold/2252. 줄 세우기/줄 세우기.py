I=lambda:map(int,input().split())
n,m=I()
p=[[]for _ in[0]*(n+1)]
q=[]
r=[]
o=[0]*(n+1)
for _ in[0]*m:
    x,y=I()
    p[x]+=y,
    o[y]+=1
for i in range(1,n+1):
    if o[i]<1:q+=i,
while q:
    x=q.pop(0)
    r+=x,
    for y in p[x]:
        o[y]-=1
        if o[y]<1:q+=y,
print(*r)