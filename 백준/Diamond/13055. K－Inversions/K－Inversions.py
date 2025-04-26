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
        for i in range(0, n, s):
            for j in range(s // 2):
                t = x[i + j + s // 2] * exp(1j * p / s * j)
                x[i + j + s // 2], x[i + j] = x[i + j] - t, x[i + j] + t
        s <<= 1
    return inv and [x / n for x in x] or x

def conv(a, b):
    m = 1 << (len(a) + len(b) - 1).bit_length()
    a = a + [0] * (m - len(a))
    b = b + [0] * (m - len(b))
    a, b = fft(a, 0), fft(b, 0)
    r = [a[i] * b[i] for i in range(m)]
    return [round(i.real) for i in fft(r, 1)]

A = [s=='A' for s in input()]
B = [not s for s in A[::-1]]
C = conv(A, B)
for i in range(len(A), 2 * len(A) - 1): print(C[i])