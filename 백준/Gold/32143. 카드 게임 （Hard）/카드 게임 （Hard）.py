from heapq import*
h,n,q,*l=map(int,open(0).read().split())
p=heappop
d=l[:n]
heapify(d)
s=sum(d)
for i in 0,*l[n:]:
    heappush(d,i)
    s+=i
    while s-d[0]>=h:s-=p(d)
    print(-1if s<h else len(d))
