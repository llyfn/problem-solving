I=lambda:map(int,input().split())
n,=I();g=[[*I()]for _ in range(n)]
M=g[0][:];m=g[0][:]
for i in range(1,n):
    a,b,c=g[i]
    M=[max(M[:2])+a,max(M)+b,max(M[1:])+c]
    m=[min(m[:2])+a,min(m)+b,min(m[1:])+c]
print(max(M),min(m))
