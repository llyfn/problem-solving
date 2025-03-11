import sys
sys.setrecursionlimit(10**5)
I=lambda:map(int,input().split())
for _ in[0]*int(input()):
    n,=I();s,v,d=[*I()],[1]*(n+1),[1]*(n+1)
    def f(x):
        v[x]=0;w=s[x-1];global n
        if v[w]:f(w)
        elif d[w]:
            while w!=x:n-=1;w=s[w-1]
            n-=1
        d[x]=0
    for i in range(1,n+1):
        if v[i]:f(i)
    print(n)