from itertools import*
n=int(input())
a={s:i for i,s in enumerate(input().split())}
print(f'{sum(a[c[0]]<a[c[1]]for c in combinations(input().split(),2))}/{n*(n-1)//2}')