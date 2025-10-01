*L,_,S=open(0).read().split()
_,*L=map(int,L)
C=[[s<"D",s.count("A")]for s in S.split('J')]
if len(C)<2:print("NO");exit()
c=0
d,a=C.pop(0)
if d*(L[1]<0)or a<L[1]:c=1
if C[-1][0]and C[-1][1]<1:C[-1][0]=d
C[-1][1]+=a
for i,x in enumerate(L[2:]):
    d,a=C[i%len(C)]
    if d*(x<0)or a<x:c=1;break
print('YNEOS'[c::2])