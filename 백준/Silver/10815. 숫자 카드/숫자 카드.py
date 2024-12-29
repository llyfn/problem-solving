_, a, _, b = [input().split() for _ in range(4)]
a = {*a}
print(*[+(i in a) for i in b])