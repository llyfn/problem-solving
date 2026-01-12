[N],A,[M],*Q=[[*map(int,i.split())]for i in open(0)]
S=int(N**.5)
R=[0]*M
C=[0]*1000001
Q=sorted([[Q[i][0]-1,Q[i][1]-1,i]for i in range(M)],key=lambda x:(x[0]//S,x[1]))
l,r,q=Q[0]
v=0
for i in range(l,r+1):v+=C[A[i]]==0;C[A[i]]+=1
R[q]=v
for i in range(1,M):
 x,y,q=Q[i]
 while x<l:l-=1;v+=C[A[l]]==0;C[A[l]]+=1
 while x>l:C[A[l]]-=1;v-=C[A[l]]==0;l+=1
 while y>r:r+=1;v+=C[A[r]]==0;C[A[r]]+=1
 while y<r:C[A[r]]-=1;v-=C[A[r]]==0;r-=1
 R[q]=v
print(*R,sep='\n')