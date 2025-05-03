M=10007
def f(n,r):
    a=b=1
    for i in range(r):a*=n-i;a%=M;b*=i+1;b%=M
    return a*pow(b,M-2,M)%M
N=int(input())
R=0
for i in range(1,N//4+1):
    R+=f(52-i*4,N-i*4)*f(13,i)*(-1)**(i-1)
    R%=M
print(R)