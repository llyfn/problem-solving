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

N = int(input())
X = [0] * N
Y = [0] * N
for i in range(1, N): X[i * i % N] += 1; Y[2 * i * i % N] += 1
X += [0] * (2 ** int(log(N, 2).real + 2) - N)
X = fft(X, 0)
for i in range(len(X)): X[i] *= X[i]
X = [round(i.real) for i in fft(X, 1)]
A = sum((X[k := i * i % N] + X[k + N] - Y[k]) // 2 + Y[k] for i in range(1, N))
print(A)