I=iter(open(0).read().split())
for _ in[0]*int(next(I)):
 n=int(next(I));G=[next(I)for _ in range(n)];H=[*map(''.join,zip(*G))]
 def S(M):
  O=[0]*10
  for d in range(10):
   k=str(d);P=[(i,x,r.rfind(k))for i,r in enumerate(M)if(x:=r.find(k))+1]
   if P:
    mn,mx=P[0][0],P[-1][0]
    for i,a,b in P:O[d]=max(O[d],(b-a)*max(i,n-1-i),max(b,n-1-a)*max(i-mn,mx-i))
  return O
 print(*[max(a,b)for a,b in zip(S(G),S(H))])