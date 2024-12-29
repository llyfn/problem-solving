import collections as c

d = c.deque(range(1, int(input()) + 1))
while len(d) > 0:
    print(d.popleft(), end=' ')
    d.rotate(-1)