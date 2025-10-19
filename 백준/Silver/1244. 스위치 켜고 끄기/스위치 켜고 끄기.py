[n],l,_,*c=[[*map(int,i.split())]for i in open(0)]
for s,k in c:
 if s>1:
  k-=1;l[k]^=1;i=1
  while(0<=k-i)*(k+i<n)and l[k-i]==l[k+i]:l[k-i]^=1;l[k+i]^=1;i+=1
 else:
  for i in range(k-1,n,k):l[i]^=1
for i in range(0,n,20):print(*l[i:i+20])