d,p,q=map(int,input().split())
if p>q:p,q=q,p
m=1e11
for i in range(min(d//q,p)+1):m=min(m,(p-(d-q*i)%p)%p)
print(d+min(m,(q-(d%q))%q))