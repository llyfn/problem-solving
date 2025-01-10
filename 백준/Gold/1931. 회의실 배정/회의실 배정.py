I=lambda:[*map(int,input().split())]
m=[(I()[::-1]) for _ in range(I()[0])]
m.sort()
n=[m.pop(0)]
for i in m:
    if i[1]>=n[-1][0]:n+=i,
print(len(n))