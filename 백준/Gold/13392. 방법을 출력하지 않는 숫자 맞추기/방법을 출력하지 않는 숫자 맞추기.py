def spin(n, c, d):
    s = [[0] * 10 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(10):
            spins = (d[i] - c[i] - j) % 10
            s[i][j] = min(spins + s[i + 1][(spins + j) % 10], 10 - spins + s[i + 1][j])
    return s[0][0]

N = int(input())
curr, dest = list(map(int, input())), list(map(int, input()))
print(spin(N, curr, dest))