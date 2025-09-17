from itertools import*
n,m,*h=map(int,open(0).read().split())
print(*(sorted({s for c in combinations(h,m)if(s:=sum(c))>1and all(s%i for i in range(2,int(s**0.5)+1))})or[-1]))