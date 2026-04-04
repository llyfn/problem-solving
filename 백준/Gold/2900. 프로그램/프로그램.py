[n,k],x,_,*q=[[*map(int,i.split())]for i in open(0)]
cnt={}
for i in x:cnt[i]=cnt.get(i,0)+1
a=[0]*n
for j,c in cnt.items():
  for i in range(0,n,j):a[i]+=c
s=[0]*(n+1)
for i in range(n):s[i+1]=s[i]+a[i]
for l,r in q:print(s[r+1]-s[l])
