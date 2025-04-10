N=int(input())
I=lambda:[[*map(int,input().split())]for _ in[0]*N]
R=range(N)
A=I()
B=I()
print(sum(+any(A[i][k]and B[k][j]for k in R)for i in R for j in R))