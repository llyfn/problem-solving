import sys
sys.setrecursionlimit(10**5)
def f(s,e):
    if s>e:return 0
    global i
    x=P[i]
    T[x]=[0,0]
    i-=1
    if s==e:return x
    j=M[x]
    T[x]=[f(j+1,e),f(s,j-1)]
    return x
def p(x):
    if x>0:print(x,end=" ");p(T[x][1]);p(T[x][0])
I=lambda:[*map(int,input().split())]
T=dict()
N,=I()
O=I()
M={v:k for k,v in enumerate(O)}
P=I()
i=N-1
p(f(0,N-1))