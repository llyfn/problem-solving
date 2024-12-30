for _ in range(int(input())):
    n = int(input())
    v = [*map(int, input().split())]
    m = int(input())
    d = [1] + [0] * m
    for x in v:
        for i in range(x, m + 1): d[i] += d[i - x]
    print(d[-1])
