from itertools import*
from bisect import*
n,m,*h=map(int,open(0).read().split())
p=[*accumulate(h[:m])]
for b in h[m:]:print(i+1if(i:=bisect_left(p,b))<m else'Go away!')