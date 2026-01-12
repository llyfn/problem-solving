[N],A,[M],*Q=[[*map(int,i.split())]for i in open(0)]
S=int(N**.5)
R=[0]*M
C=[0]*100001
T=[0]*100001
Q=sorted([[Q[i][0]-1,Q[i][1]-1,i]for i in range(M)],key=lambda x:(x[0]//S,x[1]))
l=0
r=-1
v=[0]
def F(x):T[C[x]]-=C[x]!=0;C[x]+=1;T[C[x]]+=1;v[0]=max(v[0],C[x])
def G(x):T[C[x]]-=1;v[0]-=not T[C[x]]+v[0]-C[x];C[x]-=1;T[C[x]]+=1;
for i in range(0,M):
 x,y,q=Q[i]
 while x<l:l-=1;F(A[l])
 while x>l:G(A[l]);l+=1
 while y>r:r+=1;F(A[r])
 while y<r:G(A[r]);r-=1
 R[q]=v[0]
print(*R,sep='\n')