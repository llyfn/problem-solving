import sys, math

input = sys.stdin.readline

MOD = 7 * 17 * 2 ** 23 + 1
RT = 3

def ntt(x, p, r, inv):
    n = len(x)
    j = 0
    for i in range(1, n):
        b = n >> 1
        while j & b: j ^= b; b >>= 1
        j ^= b
        if i < j: x[i], x[j] = x[j], x[i]
    s = 2
    while s <= n:
        l = pow(r, (p - 1) // s, p)
        if inv: l = pow(l, p - 2, p)
        for i in range(0, n, s):
            w = 1
            for j in range(s // 2):
                t = x[i + j + s // 2] * w
                x[i + j + s // 2], x[i + j] = (x[i + j] - t) % p, (x[i + j] + t) % p
                w = w * l % p
        s <<= 1
    if inv:
        ni = pow(n, p - 2, p)
        for i in range(n): x[i] = x[i] * ni % p

def mul(a, b, p, r):
    m = 1 << (len(a) + len(b) - 1).bit_length()
    a = a + [0] * (m - len(a))
    b = b + [0] * (m - len(b))
    ntt(a, p, r, 0)
    ntt(b, p, r, 0)
    for i in range(m): a[i] = a[i] * b[i] % p
    ntt(a, p, r, 1)
    return a

N, M = map(int, input().split())
A = input()
B = input()[::-1]
R = mul([+(i == 'R') for i in A], [+(i == 'P') for i in B], MOD, RT)
P = mul([+(i == 'P') for i in A], [+(i == 'S') for i in B], MOD, RT)
S = mul([+(i == 'S') for i in A], [+(i == 'R') for i in B], MOD, RT)
print(max([r + p + s for r, p, s in zip(R, P, S)][M:]))