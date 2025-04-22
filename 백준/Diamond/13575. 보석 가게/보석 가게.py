M = 7 * 17 * 2 ** 23 + 1

def ntt(x, inv):
    n = len(x)
    j = 0
    for i in range(1, n):
        b = n >> 1
        while j >= b: j -= b;b >>= 1
        j += b
        if i < j: x[i], x[j] = x[j], x[i]
    s = 2
    while s <= n:
        p = pow(3, (M - 1) // s, M)
        if inv: p = pow(p, M - 2, M)
        for i in range(0, n, s):
            w = 1
            for j in range(s // 2):
                t = x[i + j + s // 2] * w
                x[i + j + s // 2], x[i + j] = (x[i + j] - t) % M, (x[i + j] + t) % M
                w = w * p % M
        s <<= 1
    for i in range(n):
        if x[i] < 0: x[i] += M
    if inv:
        ni = pow(n, M - 2, M)
        for i in range(n): x[i] = x[i] * ni % M
    return x

def conv(a, b):
    m = 1 << (len(a) + len(b) - 1).bit_length()
    a = a + [0] * (m - len(a))
    b = b + [0] * (m - len(b))
    a, b = ntt(a, 0), ntt(b, 0)
    r = [a[i] * b[i] for i in range(m)]
    return [+(i > 0) for i in ntt(r, 1)]

N, K = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * (max(A) + 1)
for i in A: L[i] += 1
R = [1]
while K:
    if K & 1: R = conv(R, L)
    L = conv(L, L)
    K >>= 1
for i in range(len(R)):
    if R[i]: print(i, end=' ')