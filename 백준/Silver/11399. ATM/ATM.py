n = int(input()); l = sorted([*map(int, input().split())])
print(sum([l[i] * (n - i) for i in range(n)]))