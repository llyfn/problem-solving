def f(x):
    m = M
    for i in x:
        m[i] = m.get(i, dict())
        m = m[i]
def g(c, d):
    if len(c) == 0: return
    for k in sorted(c.keys()):
        print("--" * d, end="")
        print(k)
        g(c[k], d + 1)        
M = dict()
for _ in range(int(input())): f([*input().split()][1:])
g(M, 0)