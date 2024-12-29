l = [[*map(int, input().split())] for _ in range(int(input()))]
print(*[sum(1 for a, b in l if a > x and b > y) + 1 for x, y in l])