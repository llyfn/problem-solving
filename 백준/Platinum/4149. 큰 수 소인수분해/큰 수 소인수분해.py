import math, random, sys

sys.setrecursionlimit(10 ** 4)
def pollard_rho(n):
    def f(m):
        if m == 1: return
        if not m & 1:
            yield 2
            yield from f(m >> 1)
            return
        if miller_rabin(m):
            yield m
            return

        g = m
        while True:
            if g == m:
                x = y = random.randint(2, m - 1)
                c = random.randint(1, m - 1)
            x = (x ** 2 % m + c + m) % m
            y = (((y ** 2 % m + c + m) % m) ** 2 % m + m + c) % m
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
            if (t := pow(a, d, m)) == m - 1: return True
            elif d & 1: return t == 1 or t == m - 1
            d >>= 1

    if n in primes: return True
    elif not n & 1: return False
    for p in primes:
        if not test(n, p): return False
    return n > 40

print(*pollard_rho(int(input())), sep='\n')