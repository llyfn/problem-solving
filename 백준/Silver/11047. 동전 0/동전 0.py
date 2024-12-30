import bisect as b
n, m = map(int, input().split())
v = [int(input()) for _ in range(n)]
i = 0
while m > 0: m -= v[b.bisect_right(v, m) - 1]; i += 1
print(i)