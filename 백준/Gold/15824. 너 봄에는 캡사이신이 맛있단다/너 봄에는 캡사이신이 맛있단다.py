N,*S=map(int,open(0).read().split())
M=10**9+7
t=1
T=[0]+[(t:=2*t%M)-1for _ in[0]*N]
p=m=0
S.sort()
for i in range(N-1,0,-1):p+=S[i]*T[i];p%=M;m+=S[N-1-i]*T[i];m%=M
print((p-m)%M)