for _ in range(int(input())):
    k, n = input().split()
    print(int(k), +(max(n) < '8') and int(n, 8), int(n), int(n, 16))