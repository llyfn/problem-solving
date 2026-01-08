N=next
I=map(int,open(0).read().replace('.','').split())
while n:=N(I):
 m=N(I);d=[0]*-~m
 for _ in[0]*n:
  c=N(I);p=N(I)
  for i in range(p,m+1):d[i]=max(d[i],d[i-p]+c)
 print(d[m])