I=lambda:map(int,input().split())
N,=I()
B=[[*I()]for _ in[0]*N]
A=0
D=[0]*N*4
def f(x,a,z):
    if x>=N*N:global A;A=max(A,a);return
    r,c=divmod(x,N);p,q=r+c,r-c+3*N
    if not(D[p]or D[q]or p%2!=z)and B[r][c]:D[p]=D[q]=1;f(x+1,a+1,z);D[p]=D[q]=0
    f(x+1,a,z)
f(0,0,0)
R,A=A,0
f(1,0,1)
print(R+A)