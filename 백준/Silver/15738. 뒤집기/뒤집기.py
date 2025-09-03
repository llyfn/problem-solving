n,k,m,*l=map(int,open(0).read().split())
for i in l[n:]:
    if i>=k>0:k=i-k+1
    elif n>=k>n+i:k=2*n+i-k+1
print(k)