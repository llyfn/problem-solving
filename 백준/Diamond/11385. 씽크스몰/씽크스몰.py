MOD = 3 * 3 * 7 * 31 * 67 * 2 ** 45 + 1
RT = 5

def ntt(x, m, r, inv):
    n = len(x)
    j = 0
    for i in range(1, n):
        b = n >> 1
        while j & b: j ^= b; b >>= 1
        j ^= b
        if i < j: x[i], x[j] = x[j], x[i]
    s = 2
    while s <= n:
        p = pow(r, (m - 1) // s, m)
        if inv: p = pow(p, m - 2, m)
        for i in range(0, n, s):
            w = 1
            for j in range(s // 2):
                t = x[i + j + s // 2] * w
                x[i + j + s // 2], x[i + j] = (x[i + j] - t) % m, (x[i + j] + t) % m
                w = w * p % m
        s <<= 1
    if inv:
        ni = pow(n, m - 2, m)
        for i in range(n): x[i] = x[i] * ni % m

def mul(a, b, p, r):
    n = 1 << (len(a) + len(b) - 1).bit_length()
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    ntt(a, p, r, 0)
    ntt(b, p, r, 0)
    for i in range(n): a[i] = a[i] * b[i] % p
    ntt(a, p, r, 1)
    return a

N, M = map(int, input().split())
F = [*map(int, input().split())]
G = [*map(int, input().split())]
R = mul(F, G, MOD, RT)
A = 0
for i in range(N + M + 1): A ^= R[i]
print(A)