I=lambda:map(int,input().split())
T,=I()
for _ in[0]*T:
    N,=I()
    A=[*I()]
    B=[*range(1,N+1)]
    for i in range(N):
        B[i]+=B[i]==A[i]
        for j in range(i+1,N):
            if B[j-1]>=B[j]:
                B[j]+=B[j-1]-B[j]+1
    print(B[-1])