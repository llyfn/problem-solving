_, a, _, b = [input().split() for _ in range(4)]
c = {*a}
for i in b: print(+(i in c))