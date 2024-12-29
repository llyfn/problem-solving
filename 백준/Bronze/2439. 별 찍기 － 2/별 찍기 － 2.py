n = int(input())
print(*[f"{' ' * (n - i)}{'*' * i}" for i in range(1, n + 1)], sep='\n')
