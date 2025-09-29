n,m,*l=map(int,open(0).read().split())
M=10**9+7
g=[[]for _ in[0]*-~n]
for u,v in zip(l[::2],l[1::2]):g[u]+=[v];g[v]+=[u]
d=[0]+[1]*n
exec('d=[sum(d[k]for k in g[i])%M for i in range(n+1)];'*7)
print(sum(d)%M)