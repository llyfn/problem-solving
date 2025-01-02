import collections as c, math
for _ in range(int(input())):
    l = [input().split()[1] for _ in range(int(input()))]
    print(math.prod([i + 1 for i in c.Counter(l).values()]) - 1)
