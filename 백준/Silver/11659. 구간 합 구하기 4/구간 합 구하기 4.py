n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n-1): a[i+1] += a[i]
for _ in range(m):
    l, r = map(int, input().split())
    print(a[r-1] - a[l-2] if l > 1 else a[r-1])