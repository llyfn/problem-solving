import collections as c
s = [int(input()) for _ in range(int(input()))]
d = c.deque(); o = []; i = 1
for a in s:
    if not d or d[-1] < a:
        while i <= a:
            d.append(i)
            i += 1
            o.append('+')
    if d[-1] == a:
        d.pop()
        o.append('-')
    else:
        print('NO')
        break
else: print(*o, sep='\n')