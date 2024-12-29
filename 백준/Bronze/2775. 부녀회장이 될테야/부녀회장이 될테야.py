import math
l = [[int(input()), int(input())] for _ in range(int(input()))]
for k, n in l: print(math.comb(k + n, k + 1))
