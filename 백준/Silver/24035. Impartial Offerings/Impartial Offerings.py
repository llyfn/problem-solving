for t in range(int(input())):
    n = int(input())
    s = sorted(map(int, input().split()))
    a = r = 1
    for i in range(1, n):
        if s[i] > s[i-1]: r += 1
        a += r
    print(f'Case #{t + 1}: {a}')
