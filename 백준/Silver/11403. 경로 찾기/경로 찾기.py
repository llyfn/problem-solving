n=int(input())
g=[[*map(int,input().split())]for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if g[j][i] and g[i][k]:g[j][k]=1
for i in g:print(*i)