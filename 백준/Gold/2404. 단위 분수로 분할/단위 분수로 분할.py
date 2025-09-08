from math import*
def f(p,q,a,n,k):
    if n<1:return 0
    c=0
    for d in range(max(k,(q+p-1)//p),min(a,n*q//p)+1):
        x=p*d-q
        if x==0:c+=1
        else:y=q*d;g=gcd(x,y);c+=f(x//g,y//g,a//d,n-1,d)
    return c
print(f(*map(int,input().split()),1))