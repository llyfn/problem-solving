n,l,*A=open(0).read().split()
s=A[0]
for t in[s]+[s[:i]+chr(c)+s[i+1:]for i in range(int(l))for c in range(65,91)]:
    if all(sum(x!=y for x,y in zip(t,k))<2for k in A):print(t);break
else:print("CALL FRIEND")