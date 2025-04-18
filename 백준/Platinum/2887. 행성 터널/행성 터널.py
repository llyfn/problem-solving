N,*L=map(int,open(0).read().split())
s,e=sorted,enumerate
X,Y,Z=L[::3],L[1::3],L[2::3]
X=s((x,i)for i,x in e(X))
Y=s((y,i)for i,y in e(Y))
Z=s((z,i)for i,z in e(Z))
G=[]
for i in range(N-1):G+=(X[i+1][0]-X[i][0],X[i][1],X[i+1][1]),(Y[i+1][0]-Y[i][0],Y[i][1],Y[i+1][1]),(Z[i+1][0]-Z[i][0],Z[i][1],Z[i+1][1]),
G.sort()
P,C=[*range(N)],0
def f(x):
    if P[x]!=x:P[x]=f(P[x])
    return P[x]
for w,a,b in G:
    if (m:=f(a))!=(n:=f(b)):
        if m<n:P[n]=m
        else:P[m]=n
        C+=w
print(C)