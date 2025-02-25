n,m=map(int,input().split())
a=sorted([int(input()) for _ in range(n)])
def f(x):
    i,s,e=n,0,n
    while s<e:
        M=(s+e)//2
        if a[M]<x:s=M+1
        elif a[M]>x:e=M
        else:i=min(i,M);e=M
    return i if i<n else -1
for _ in range(m):print(f(int(input())))