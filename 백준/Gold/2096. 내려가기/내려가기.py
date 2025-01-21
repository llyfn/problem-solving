I=lambda:map(int,input().split())
n,=I()
g=[[*I()]for _ in range(n)]
M=m=[0]*3
for a,b,c in g:M=[max(M[:2])+a,max(M)+b,max(M[1:])+c];m=[min(m[:2])+a,min(m)+b,min(m[1:])+c]
print(max(M),min(m))
