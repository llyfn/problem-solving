import math
import random

def solve(n):
    if not legendre(n): return 4
    elif not fermat(n): return 3
    else: return 1 if perfect_square(n) else 2

def legendre(n):
    while not n % 4: n //= 4
    return n % 8 != 7

def fermat(n):
    s = set()
    for i in pollard_rho(n):
        if i in s: s.remove(i)
        else: s.add(i)
    for i in s:
        if i % 4 == 3: return False
    return True

def perfect_square(n):
    return n == math.isqrt(n) ** 2

def pollard_rho(n):
    def f(m):
        if m == 1: return
        if not m & 1: yield 2; yield from f(m >> 1); return
        if miller_rabin(m): yield m; return

        g = m
        while True:
            if g == m:
                x = y = random.randint(0, m - 3) + 2
                c = random.randint(0, 19) + 1
            x = (x ** 2 + c) % m
            y = ((y ** 2 + c) % m) ** 2 + c % m
            g = math.gcd(abs(x - y), m)
            if g != 1: break
        yield from f(g)
        yield from f(m // g)

    return sorted(f(n))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
def miller_rabin(n):
    def test(m, a):
        if m % a == 0: return False
        d = m - 1
        while True:
            if (t := pow(a, d, m)) == 1 or t == m - 1: return True
            elif d & 1: return False
            d >>= 1

    if n in primes: return True
    elif not n & 1: return False
    for p in primes:
        if not test(n, p): return False
    return n > 40

print(solve(int(input())))