n=int(input());s=input()
A=len(set(s))
T=[(1,0,0)]
for j in range(1,A+1):
 C={};i=m=b=0;a=0
 for k in range(n):
   c=s[k];C[c]=C.get(c,0)+1
   while len(C)>j:
    l=s[i];C[l]-=1;i+=1
    if C[l]==0:del C[l]
   L=k-i+1
   if L>m:m=L;b=i;a=len(C)
 if m:T+=(a/m,b,b+m-1),
m,L,R=min(T)
print(L+1,R+1)