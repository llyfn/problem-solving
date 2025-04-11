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

N, *L = map(int, open(0).read().split())
X, Y = L[:N] * 2, L[-1:N-1:-1]
n = 1 << (len(X) + len(Y) - 1).bit_length()
X += [0] * (n - len(X))
Y += [0] * (n - len(Y))
X = fft(X, 0)
Y = fft(Y, 0)
for i in range(n): X[i] *= Y[i]
X = fft(X, 1)

print(round(max(x.real for x in X)))