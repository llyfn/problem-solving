N, M = map(int, input().strip().split())

def flip(x):
    if x == 0:
        return 1
    else:
        return 0

A = [list(map(int, list(input().strip()))) for _ in range(N)]
B = [list(map(int, list(input().strip()))) for _ in range(N)]

cnt = 0
if N >= 3 and M >= 3:
    for n in range(N-2):
        for m in range(M-2):
            if A[n][m] != B[n][m]:
                cnt += 1
                for i in range(3):
                    for j in range(3):
                        A[n+i][m+j] = flip(A[n+i][m+j])

for n in range(N):
    if A[n][M-2] != B[n][M-2] or A[n][M-1] != B[n][M-1]:
        cnt = -1
        break
for m in range(M-2):
    if A[N-2][m] != B[N-2][m] or A[N-1][m] != B[N-1][m]:
        cnt = -1
        break

print(cnt)