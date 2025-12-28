from bisect import*
M=100005
L=[*range(M)]
for i in L[2:320]:
 if L[i]:L[i*i::i]=[0]*len(L[i*i::i])
P=[x for x in L if x>1]
E,O=[0],[0]
for i,x in enumerate(P):E+=E[-1]+x*(i%2^1),;O+=O[-1]+x*(i%2),
D=[*map(int,open(0).read().split())]
for a,b in zip(D[1::2],D[2::2]):
 l=bisect_left(P,a);r=bisect_right(P,b);e=E[r]-E[l];o=O[r]-O[l]
 print(3*o-e if l%2 else 3*e-o)