from heapq import*
N,*P,D=map(int,open(0).read().split())
P=sorted(sorted(i)[::-1]for i in zip(P[::2],P[1::2]))
R,Q=0,[]
for a,b in P:heappush(Q,b);Q and a-D>Q[0]and heappop(Q);R=max(R,len(Q))
print(R)