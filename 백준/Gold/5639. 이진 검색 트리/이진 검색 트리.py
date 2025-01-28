import sys
sys.setrecursionlimit(10**9)
n=[*map(int,open(0).readlines())]
def f(s,e):
    if s>e:return
    m=e+1
    for i in range(s+1,e+1):
        if n[s]<n[i]:m=i;break
    f(s+1,m-1);f(m,e);print(n[s])
f(0,len(n)-1)