import heapq, sys
I = lambda: int(sys.stdin.readline())
m = []
for _ in range(I()):
    if i := I(): heapq.heappush(m, -i)
    else: print(-heapq.heappop(m) if m else 0)
