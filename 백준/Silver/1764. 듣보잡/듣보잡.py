n, m = map(int, input().split())
l = sorted({input() for _ in range(n)} & {input() for _ in range(m)})
print(len(l), *l, sep='\n')