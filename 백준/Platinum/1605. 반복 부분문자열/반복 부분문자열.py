input()
s=input()
n=len(s)
R=[ord(c)for c in s]
S=[*range(n)]
k=1
while k<n:
 g=lambda i:(R[i],R[i+k]if i+k<n else-1)
 S.sort(key=g)
 N=[0]*n;r=N[S[0]]=0
 for i in range(1,n):p,c=S[i-1],S[i];r+=g(p)!=g(c);N[c]=r
 R=N
 if r==n-1:break
 k*=2
L=[0]*n
I=[0]*n
for i in range(n):I[S[i]]=i
h=0
for i in range(n):
 if I[i]==0:h=0
 else:
  j=S[I[i]-1]
  while i<n-h>j and s[i+h]==s[j+h]:h+=1
  L[I[i]]=h;h-=h>0
print(max(L))