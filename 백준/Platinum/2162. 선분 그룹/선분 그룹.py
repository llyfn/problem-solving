from collections import*
I=lambda:[*map(int,input().split())]
N,=I()
L=[I()for _ in[0]*N]
F=lambda x,y,z,u,v,w:(w-y)*(z-x)-(u-y)*(v-x)
def G(a,b,c,d,e,f,g,h):
    P,Q=F(a,b,c,d,e,f)*F(a,b,c,d,g,h),F(e,f,g,h,a,b)*F(e,f,g,h,c,d)
    return min(a,c)<=max(e,g)and min(e,g)<=max(a,c)and min(b,d)<=max(f,h)and min(f,h)<=max(b,d)if P==Q==0else P<=0and Q<=0
s=[*range(N)]
def H(x):
    if s[x]!=x:s[x]=H(s[x])
    return s[x]
def K(x,y):
    x,y=H(x),H(y)
    if x>y:s[x]=y
    else:s[y]=x
for i in range(N):
    for j in range(i+1,N):
        if G(*L[i],*L[j]):K(i,j)
C=Counter([H(i)for i in s])
print(len(C))
print(max(C.values()))