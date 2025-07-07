import sys, math

input = sys.stdin.readline

MOD = 5 * 31 * 2 ** 23 + 1
RT = 3
N = 1_000_000

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

prime = [0] * 2 + [1] * N
for i in range(2, 1001):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = 0
A = [0] * (N // 2 + 1)
B = [0] * (N // 2 + 1)
for i in range(3, N + 1):
    if prime[i]:
        A[(i - 1) // 2] = B[(i - 1) // 2] = 1
R = mul(A, B, MOD, RT)
for i in range(int(input())):
    n = int(input())
    if n == 4: print(1)
    else: print((R[n // 2 - 1] + 1) // 2)