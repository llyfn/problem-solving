I=lambda:[*map(int,input().split())]
n,m=I()
t={*I()[1:]}
p=[{*I()[1:]}for _ in range(m)]
for _ in range(m):
    for q in p:
        if t&q:t|=q
print(sum([0 if t&q else 1 for q in p]))