from math import isqrt, gcd
from random import randint

def solve_four(n):
    m = 1
    while not n % 4: n //= 4; m *= 2
    a, b, c = solve_three(n - 1)
    return m, a * m, b * m, c * m
def solve_three(n):
    f = dict()
    m, l = 1, 1
    for i in pollard_rho(n): f[i] = f.get(i, 0) + 1
    for i in f:
        m *= i ** (f[i] >> 1)
        if f[i] & 1: l *= i
    t = 1
    while squares(l - t * t) != 2: t += 1
    a, b = solve_two(l - t * t)
    return a * m, b * m, t * m
def solve_two(n):
    f = dict()
    m, l = 1, []
    for i in pollard_rho(n): f[i] = f.get(i, 0) + 1
    for i in f:
        if f[i] & 1: l.append(i)
        m *= i ** (f[i] >> 1)
    x, y = 1, 0
    for i in l:
        c = cornacchia(i, 1) if i != 2 else (1, 1)
        a, b = c
        x, y = x * b + y * a, abs(x * a - y * b)
    return x * m, y * m
def cornacchia(m, d):
    r1, r2 = m, tonelli_shanks(m - d, m)
    while r1 * r1 > m: r1, r2 = r2, r1 % r2
    r2 = isqrt((m - r1 * r1) // d)
    return r1, r2
def tonelli_shanks(n, p):
    q, s = p - 1, 0
    while not q & 1: q >>= 1; s += 1
    z = randint(2, p - 1)
    while pow(z, p - 1 >> 1, p) == 1: z = randint(2, p - 1)
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, q + 1 >> 1, p)
    while t != 0 and t != 1:
        k = t
        i = 0
        while k % p != 1:
            k = k * k % p
            i += 1
        b = pow(c, 1 << m - i - 1, p)
        m = i
        c = b * b % p
        t = t * c % p
        r = r * b % p
    return r * t
def squares(n):
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
    return n == isqrt(n) ** 2
def pollard_rho(n):
    def f(m):
        if m == 1: return
        if not m & 1: yield 2; yield from f(m >> 1); return
        if miller_rabin(m): yield m; return
        g = m
        while True:
            if g == m:
                x = y = randint(0, m - 3) + 2
                c = randint(0, 19) + 1
            x = (x ** 2 + c) % m
            y = ((y ** 2 + c) % m) ** 2 + c % m
            g = gcd(abs(x - y), m)
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

N = int(input())
num = squares(N)
print(num)
if num == 1: print(isqrt(N))
elif num == 2: print(*sorted(solve_two(N)))
elif num == 3: print(*sorted(solve_three(N)))
elif num == 4: print(*sorted(solve_four(N)))