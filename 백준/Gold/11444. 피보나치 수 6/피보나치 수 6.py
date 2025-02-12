m,d=10**9+7,{0:0,1:1,2:1}
def f(x):
    if x not in d:y=x//2;d[x]=(f(y)**2+f(y+1)**2)%m if x&1 else f(y)*(f(y)+2*f(y-1))%m
    return d[x]
print(f(int(input())))
