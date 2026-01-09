N=next;I=iter(open(0).read().split())
for t in range(int(N(I))):
 R,C=int(N(I)),int(N(I));G=[]
 for _ in[0]*R:
  r=list(N(I));k=[c for c in r if c>'?']
  if k:
   v=k[0]
   for j in range(C):r[j]=v=r[j]if r[j]>'?'else v
  G+=r,
 v=[r for r in G if r[0]>'?'][0]
 print(f"Case #{t+1}:")
 for r in G:print(*(v:=r if r[0]>'?'else v),sep='')