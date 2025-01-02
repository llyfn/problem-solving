l = [int(input()) for _ in range(int(input()))]
p = [1, 1, 1] + [0] * max(l)
for i in range(3, len(p)): p[i] = p[i-2] + p[i-3]
print(*[p[i - 1] for i in l], sep='\n')
