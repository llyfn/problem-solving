from cmath import*
n,*a=map(int,open(0).read().split())
def f(x,v):
    n,j=len(x),0
    for i in range(1,n):
        b=n>>1
        while j>=b:j-=b;b>>=1
        j+=b
        if i<j:x[i],x[j]=x[j],x[i]
    p,s=(2-4*v)*pi,2
    while s<=n:
        z=exp(1j*p/s)
        for i in range(0,n,s):
            w=1
            for j in range(i,i+s//2):
                t=x[j+s//2]*w
                x[j+s//2],x[j]=x[j]-t,x[j]+t
                w*=z
        s<<=1
    return v and[x/n for x in x]or x
K=1<<19
x=[0]*K
x[0]=1
for i in a[:n]:x[i]=1
x=f(x,0)
for i in range(K):x[i]*=x[i]
x=f(x,1)
print(sum(round(x[i].real)and 1for i in a[n+1:]))