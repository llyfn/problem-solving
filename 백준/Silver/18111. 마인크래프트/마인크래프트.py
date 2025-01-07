import sys
I = lambda: map(int, sys.stdin.readline().split())
n, m, b = I()
a = [[*I()] for _ in range(n)]
T = R = 1e9
for i in range(min(map(min, a)), max(map(max, a))+1):
    t = r = 0
    for x in a:
        for y in x:
            if y>i: t += 2*(y-i); r += y-i
            else: t += i-y; r -= i-y
    if r + b < 0: break
    if t <= T: T = t; R = i
print(T, R)