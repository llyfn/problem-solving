import collections as c
n, k = map(int, input().split())
d = c.deque(range(1, n+1))
s = []
while d:
    d.rotate(1 - k)
    s.append(d.popleft())
print(f'<{", ".join(map(str, s))}>')