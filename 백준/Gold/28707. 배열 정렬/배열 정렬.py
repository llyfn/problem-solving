import heapq as h
P=h.heappush
I=lambda:tuple(map(int,input().split()))
N,=I()
A=I()
M,=I()
O=[I()for _ in[0]*M]
V,C,Q=set(),{A:0},[(0,A)]
while Q:
    v,a=h.heappop(Q)
    if a in V:continue
    for l,r,c in O:
        t=[*a];t[l-1],t[r-1]=t[r-1],t[l-1];t=tuple(t)
        if t not in C or C[t]>v+c:C[t]=v+c;P(Q,(v+c,t))
    V.add(a)
print(C.get(tuple(sorted(A)),-1))