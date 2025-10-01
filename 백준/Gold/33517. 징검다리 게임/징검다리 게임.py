from bisect import bisect_left as b
from itertools import*
N=lambda:exit(print("NO"))
*l,s=open(0).read().split()
n,*a,k=map(int,l)
J,D,I=[],[],[]
for i,x in enumerate(s):
    if'J'==x:J+=i,
    elif'D'==x:D+=i,
    elif'A'==x:I+=i,
if not J:N()
C=[0,*accumulate(x=='A'for x in s)];T=C[k]
p=c=0;V=set()
while p<n-1:
    if c in V:N()
    V.add(c);o=a[p+1]
    if o>0:
        if not T:N()
        j=-1;S=T-C[c]
        if(i:=b(J,c))<len(J):j=J[i]
        if o<=S:
            c=b(C,C[c]+o,c+1)
            if~j and j<c:N()
        else:
            c=b(C,(o-S-1)%T+1)
            if~j or J[0]<c:N()
        a[p+1]=0
    elif o<0:
        m=[]
        for l,t in(D,'D'),(J,'J'),(I,'A'):
            if l:i=b(l,c);x=l[0]if i==len(l)else l[i];m+=[(((x-c+k)%k),t,x)]
        if m and min(m)[1]=='D':a[p+1]=0;c=min(m)[2]+1
        else:N()
    else:i=b(J,c);c=(J[i]if i<len(J)else J[0])+1;p+=1;V=set()
    c%=k
print("YES")