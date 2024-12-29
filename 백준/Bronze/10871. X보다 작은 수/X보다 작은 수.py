n, x = map(int, input().split())
print(*[i for i in map(int, input().split()) if i < x])