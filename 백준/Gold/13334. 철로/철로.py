from heapq import*
N,*P,D=map(int,open(0).read().split())
P=sorted([sorted(P[i:i+2])for i in range(0,N*2,2)],key=lambda x:(x[1],x[0]))
R,Q=0,[]
for i in P:
    heappush(Q,i[0])
    while(Q):
        if i[1]-Q[0]>D:heappop(Q)
        else:break
    R=max(R,len(Q))
print(R)