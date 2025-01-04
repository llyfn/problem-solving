from collections import deque

n = int(input())
a = [*map(int, input().split())]
d = deque()

for i in range(1, n + 1):
    if a[-i] == 1: d.appendleft(i)
    elif a[-i] == 2: d.insert(1, i)
    else: d.append(i)

print(*d)
