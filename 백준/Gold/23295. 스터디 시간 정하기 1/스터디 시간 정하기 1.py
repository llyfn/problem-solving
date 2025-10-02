[n,t],*l=[[*map(int,i.split())]for i in open(0)if' 'in i]
a=[0]*(M:=9**6)
for s,e in l:a[s]+=1;a[e]-=1
exec('for i in range(1,M):a[i]+=a[i-1]\n'*2)
p=q=0
for i in range(t,M):
    if(r:=a[i-1]-(i>t)*a[i-t-1])>q:q,p=r,i
print(p-t,p)