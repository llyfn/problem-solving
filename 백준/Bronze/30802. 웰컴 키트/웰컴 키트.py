n = int(input()); l = list(map(int, input().split())); t, p = map(int, input().split())
print(sum([s // t + (1 if s % t else 0) for s in l])); print(n // p, n % p)