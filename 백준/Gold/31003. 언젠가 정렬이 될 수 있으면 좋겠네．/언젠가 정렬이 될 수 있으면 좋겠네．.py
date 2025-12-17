import math
n,*a=map(int,open(0).read().split())
for i in range(n):
 t=k=i
 while k*(math.gcd(a[i],a[k-1])<2):
  if a[k:=k-1]>a[i]:t=k
 a.insert(t,a.pop(i))
print(*a)