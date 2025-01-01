a = input(); b = input(); p = len(a); q = len(b)
d = [[0] * (q + 1) for _ in range(p + 2)]
for i in range(p):
    for j in range(q):
        if a[i] == b[j]: d[i + 1][j + 1] = d[i][j] + 1
        else: d[i + 1][j + 1] = max(d[i][j + 1], d[i + 1][j])
c = d[p][q]; seq = ''
while c:
    if d[p][q] == d[p - 1][q]: p -= 1
    elif d[p][q] == d[p][q - 1]: q -= 1
    else: seq += a[p - 1]; c -= 1; p -= 1; q -= 1
print(seq[::-1])
