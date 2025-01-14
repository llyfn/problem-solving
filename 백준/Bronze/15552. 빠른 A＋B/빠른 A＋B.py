import sys
I=lambda:map(int,sys.stdin.readline().split())
for _ in range(next(I())):print(sum(I()))