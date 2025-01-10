def f(n,r,c):
    if n==0:return 0
    m=1<<n-1;k=m*m
    return 3*k+f(n-1,r-m,c-m) if r>=m and c>=m else 2*k+f(n-1,r-m,c) if r>=m else k+f(n-1,r,c-m) if c>=m else f(n-1,r,c)
print(f(*map(int,input().split())))