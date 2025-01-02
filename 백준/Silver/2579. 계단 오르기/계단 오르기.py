n, *s = map(int, open(0))
l = s[:]
if n > 1: l[1] += s[0]
if n > 2: l[2] += max(s[0], s[1])
for i in range(3, n): l[i] = max(l[i-2], l[i-3]+s[i-1]) + s[i]
print(l[-1])
