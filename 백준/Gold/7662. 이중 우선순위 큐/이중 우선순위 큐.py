import sys, heapq as h
I=sys.stdin.readline
P=h.heappop
for _ in range(int(I())):
    k=int(I())
    M,m,c=[],[],dict()
    for i in range(k):
        o,a=I().split()
        a=int(a)
        if o=='I':
            h.heappush(m,a)
            h.heappush(M,-a)
            c[a]=c.get(a,0)+1
        elif a<0 and m:c[P(m)]-=1
        elif a>0 and M:c[-P(M)]-=1
        while m and c[m[0]]<1:P(m)
        while M and c[-M[0]]<1:P(M)
    print(-M[0],m[0]) if m else print('EMPTY')
