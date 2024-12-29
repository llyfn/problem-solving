k, n = map(int, input().split())
c = [int(input()) for _ in range(k)]
l = m = 0; r = max(c) * 2
while l <= r:
    m = (l + r) // 2
    if sum([x // m for x in c]) >= n: l = m + 1
    else: r = m - 1
print(r)