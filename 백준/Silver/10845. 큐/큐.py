import collections as c
d = c.deque()
for _ in range(int(input())):
    c, *n = input().split()
    if c == 'push': d.append(int(n[0]))
    elif c == 'pop': print(d.popleft() if d else -1)
    elif c == 'size': print(len(d))
    elif c == 'empty': print(+(not d))
    elif c == 'front': print(d[0] if d else -1)
    elif c == 'back': print(d[-1] if d else -1)