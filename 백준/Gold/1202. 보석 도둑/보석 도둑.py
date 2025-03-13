import heapq as h
P=h.heappop
I=lambda:[*map(int,input().split())]
n,k=I()
m=sorted([I()for _ in[0]*n])
c=sorted([int(input())for _ in[0]*k])
r=0;q=[]
for i in c:
    while m and m[0][0]<=i:h.heappush(q,-P(m)[1])
    if q:r-=P(q)
print(r)