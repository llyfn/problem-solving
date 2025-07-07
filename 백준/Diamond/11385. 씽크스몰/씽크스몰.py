P1 = 5 * 31 * 2 ** 23 + 1
R1 = 3
P2 = 3 * 17 * 2 ** 25 + 1
R2 = 29

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
F = [*map(int, input().split())]
G = [*map(int, input().split())]
C1 = mul(F, G, P1, R1)
C2 = mul(F, G, P2, R2)
A = 0
MI = pow(P1, P2 - 2, P2)
for i, j in zip(C1, C2): A ^= i + P1 * ((j - i) * MI % P2)
print(A)