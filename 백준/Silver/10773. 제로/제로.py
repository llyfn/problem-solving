import collections as c

d = c.deque()
for _ in range(int(input())):
    if (i := int(input())) == 0:
        if d: d.pop()
    else: d.append(i)
print(sum(d))