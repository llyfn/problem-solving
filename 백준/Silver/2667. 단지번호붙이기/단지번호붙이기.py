n=int(input())
m=[[*input()]for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
k,l=0,[]
def f(x,y):
    if x<0 or x>=n or y<0 or y>=n or m[x][y]=='0':return 0
    m[x][y]='0';global k;k+=1
    for d in range(4):f(x+dx[d],y+dy[d])
    return 1
for i in range(n):
    for j in range(n):
        if f(i,j):l+=k,;k=0
print(len(l),*sorted(l),sep='\n')