import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
c = [input() for _ in range(n)]
s = next((i,j.index('I')) for i,j in enumerate(c) if 'I' in j)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
v=[[0]*m for _ in range(n)]
a = 0
def f(x,y):
    v[x][y]=1
    if c[x][y]=='P':global a;a+=1
    for i in range(4):
        if 0<=(p:=x+dx[i])<n and 0<=(q:=y+dy[i])<m and not v[p][q] and c[p][q]!='X':f(p,q)
f(*s)
print(a or 'TT')