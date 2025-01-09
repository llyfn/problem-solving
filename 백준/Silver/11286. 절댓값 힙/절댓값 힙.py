import heapq as h
n,*s=map(int,open(0))
l=[]
for i in s:
    if i:h.heappush(l,(abs(i),i))
    else:print(l and h.heappop(l)[1]or 0)