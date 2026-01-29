from math import*
a,b=map(int,input().split())
n=isqrt(b)-isqrt(a)
if n<1:print(0)
else:d=gcd(n,b-a);print(f'{n//d}/{(b-a)//d}')