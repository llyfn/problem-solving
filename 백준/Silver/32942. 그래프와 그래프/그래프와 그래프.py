a,b,c=map(int,input().split())
r=[[]for _ in[0]*10]
for i in range(1,11):
    for j in range(1,11):
        if a*i+b*j==c:r[i-1]+=j,
    if not r[i-1]:r[i-1]+=0,
for i in r:print(*i)