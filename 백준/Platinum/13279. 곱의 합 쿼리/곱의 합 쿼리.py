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
    return [round(i.real) % 100003 for i in fft(r, 1)]

def mul(x, l, r):
    if l == r: return x[l]
    return conv(mul(x, l, (l + r) // 2), mul(x, (l + r) // 2 + 1, r))

N = int(input())
A = [[*i] for i in zip(map(int, input().split()), [1] * N)]
K = [int(input()) for _ in range(int(input()))]
R = mul(A, 0, N - 1)
for k in K: print(R[N - k] % 100003)