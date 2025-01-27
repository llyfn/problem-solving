N=int(input())
t=[[' ']*2*N for _ in range(N)]
def f(n,x,y):
    if n<4:
        t[x][y]=t[x+1][y-1]=t[x+1][y+1]='*'
        for i in range(-2,3):t[x+2][y+i]='*'
    else:f(k:=n//2,x,y);f(k,x+k,y-k);f(k,x+k,y+k)
f(N,0,N-1)
for i in t:print(*i,sep='')