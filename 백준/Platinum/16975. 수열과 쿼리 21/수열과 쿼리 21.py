[n], A, [m], *ops = [[*map(int, i.split())] for i in open(0)]
A = [0, *A]
tree = [0] * (n + 2)
for op, *arg in ops:
    if op == 1:
        i, j, val = arg
        while i <= n: tree[i] += val; i += i & -i
        j += 1
        while j <= n: tree[j] -= val; j += j & -j
    if op == 2:
        i = arg[0]
        diff = 0
        while i > 0: diff += tree[i]; i -= i & -i
        print(A[arg[0]] + diff)