import math
a,b=map(int,input().split())
f=lambda x:0 if x<1 else (n:=int(math.log2(x)))*(m:=1<<n)//2+f(x-m)+x-m+1
print(f(b)-f(a-1))