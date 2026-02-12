[N, P], T, K = [[*map(int, i.split())] for i in open(0)]
print(sum(T) + (P - 1) * max(T))