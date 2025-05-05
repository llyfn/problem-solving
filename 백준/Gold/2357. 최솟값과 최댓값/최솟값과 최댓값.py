from math import*
N,M,*L=map(int,open(0).read().split())
I=L[:N]
P=zip(L[N:][::2],L[N+1:][::2])
S=[0]*(1<<ceil(log2(N)+1))
def g(i,s,e):
    if s==e:S[i]=(I[s],I[s]);return S[i]
    l=g(i*2,s,m:=(s+e)//2);r=g(i*2+1,m+1,e);S[i]=(min(l[0],r[0]),max(l[1],r[1]));return S[i]
def f(i,s,e):
    if e<a or b<s:return 1<<31,0
    if a<=s and e<=b:return S[i]
    l=f(i*2,s,m:=(s+e)//2);r=f(i*2+1,m+1,e);return min(l[0],r[0]),max(l[1],r[1])
g(1,0,N-1)
for a,b in P:a-=1;b-=1;print(*f(1,0,N-1))