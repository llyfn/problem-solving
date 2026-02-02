import math

m, M = map(int, input().split())
c = M - m + 1
s = [1] * c
i = 2
while i * i <= M:
    r = math.ceil(m / i ** 2)
    while (k := r * i * i) <= M:
        if s[k - m]:
            s[k - m] -= 1
            c -= 1
        r += 1
    i += 1
print(c)