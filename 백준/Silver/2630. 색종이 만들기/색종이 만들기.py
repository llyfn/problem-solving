import sys
I = lambda: [*map(int, sys.stdin.readline().split())]
n = I()[0]; m = [I() for _ in range(n)]
w = b = 0
def f(s, i, j):
    global w, b
    if not (c := sum([m[i + k][j + l] for k in range(s) for l in range(s)])): w += 1
    elif c == s * s: b += 1
    else: s //= 2; f(s, i, j); f(s, i + s, j); f(s, i, j + s); f(s, i + s, j + s)
f(n, 0, 0)
print(w, b, sep='\n')
