from cmath import *

def fft(x, inv):
    n = len(x)
    j = 0
    for i in range(1, n):
        b = n >> 1
        while j >= b: j -= b;b >>= 1
        j += b
        if i < j: x[i], x[j] = x[j], x[i]
    p, s = (2 - 4 * inv) * pi, 2
    while s <= n:
        z = exp(1j * p / s)
        for i in range(0, n, s):
            w = 1
            for j in range(i, i + s // 2):
                t = x[j + s // 2] * w
                x[j + s // 2], x[j] = x[j] - t, x[j] + t
                w *= z
        s <<= 1
    return inv and [x / n for x in x] or x

def mul(a, b):
    m = 1 << (len(a) + len(b) - 1).bit_length()
    a = a + [0] * (m - len(a))
    b = b + [0] * (m - len(b))
    a, b = fft(a, 0), fft(b, 0)
    r = [a[i] * b[i] for i in range(m)]
    return [round(i.real) for i in fft(r, 1)]

N, *A = map(int, open(0).read().split())
A = [*zip(A[::2], A[1::2])]
M = max(A, key=lambda x: x[1])[1]
D = [0] * (M + 1)
for i in range(1, M + 1):
    for j in range(i, M + 1, i): D[j] += 1
R = mul(D, D)
R[1] = 1
for l, h in A:
    X = R[l:h + 1]
    print(R.index(m := max(X)), m)