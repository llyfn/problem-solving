import sys
sys.setrecursionlimit(10**6)
N,*S=map(int,open(0).read().split())
E=[[]for _ in[0]*(N+1)]
D=[[1,0]for _ in[0]*(N+1)]
for u,v in zip(S[::2],S[1::2]):E[u]+=v,;E[v]+=u,
def f(u,p):
    for v in E[u]:
        if v!=p:f(v,u);D[u][0]+=min(D[v]);D[u][1]+=D[v][0]
f(1,0)
print(min(D[1]))