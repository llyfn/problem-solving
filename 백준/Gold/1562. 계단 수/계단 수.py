N=int(input())
M=10**9
d=[[[0]*1024for _ in[0]*10]for _ in[0]*N]
for i in range(1,10):d[0][i][1<<i]=1
for i in range(1,N):
    for b in range(1024):
        d[i][0][b|1]+=d[i-1][1][b]
        d[i][9][b|512]+=d[i-1][8][b]
        for j in range(1,9):d[i][j][b|2**j]+=(d[i-1][j-1][b]+d[i-1][j+1][b])%M
print(sum(d[N-1][j][1023]for j in range(10))%M)