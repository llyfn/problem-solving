n,s=int(input()),input()
m=1
l=r=0
for i in range(n):
 U=set()
 for j in range(i,n):
  U.add(s[j])
  c=len(U)/(j-i+1)
  if c<m:m,l,r=c,i,j
print(l+1,r+1)