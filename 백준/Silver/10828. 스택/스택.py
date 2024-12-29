import collections as c
d = c.deque()
for _ in range(int(input())):
    c, *n = input().split()
    if c == 'push': d.append(int(n[0]))
    elif c == 'pop': print(d.pop() if d else -1)
    elif c == 'size': print(len(d))
    elif c == 'empty': print(+(not d))
    elif c == 'top': print(d[-1] if d else -1)