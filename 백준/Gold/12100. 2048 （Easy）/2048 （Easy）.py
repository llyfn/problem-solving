N=int(input())
B=[[*map(int,input().split())]for _ in[0]*N]
R=0
def f(b,d,k):
    for i in range(N):
        c=(N-d)%N
        for j in range(N-1,-1,-1)if d else range(1,N):
            if not k and b[i][j]:
                t=b[i][j];b[i][j]=0
                if b[i][c]==0:b[i][c]=t
                elif b[i][c]==t:b[i][c]*=2;c+=1-2*d
                else:c+=1-2*d;b[i][c]=t
            if k and b[j][i]:
                t=b[j][i];b[j][i]=0
                if b[c][i]==0:b[c][i]=t
                elif b[c][i]==t:b[c][i]*=2;c+=1-2*d
                else:c+=1-2*d;b[c][i]=t
def dfs(n,b):
    if n==5:global R;R=max(R,*[max(i)for i in b]);return
    for i in range(4):f(z:=[x[:]for x in b],i%2,i//2);dfs(n+1,z)
dfs(0,B)
print(R)