def g(l,r,i):
    if l==r:T[i]=(A[l],l)
    else:T[i]=min(g(l,m:=(l+r)//2,i*2),g(m+1,r,i*2+1))
    return T[i]
def f(s,e,i,l,r):
    if e<l or r<s:return 10**10,100001
    if s<=l and r<=e:return T[i]
    return min(f(s,e,i*2,l,m:=(l+r)//2),f(s,e,i*2+1,m+1,r))
def h(l,r,i,k,v):
    if k<l or r<k:return T[i]
    if l==r:T[i]=(v,k);return T[i]
    T[i]=min(h(l,m:=(l+r)//2,i*2,k,v),h(m+1,r,i*2+1,k,v))
    return T[i]
I=lambda:[*map(int,input().split())]
N,=I()
A=I()
T=[0]*(4*N)
g(0, N - 1, 1)
M,=I()
for _ in[0]*M:
    o,a,b=I()
    if o<2:h(0,N-1,1,a-1,b)
    else:c,d=f(a-1,b-1,1,0,N-1);print(d+1)