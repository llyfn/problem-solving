from itertools import*
r=[int(str(x)+str(y))for x,y in permutations(sorted([*map(int,open(0))][1:])[:4],2)]
r.sort()
print(r[2])