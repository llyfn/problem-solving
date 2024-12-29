l = [input().split() for _ in range(int(input()))]
for n, s in l: print(*[c * int(n) for c in s], sep='')