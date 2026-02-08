from heapq import *
n, *h = map(int, open(0))
heapify(h)
r = 0
while len(h) > 1: i, j = heappop(h), heappop(h); r += i + j; heappush(h, i + j)
print(r)