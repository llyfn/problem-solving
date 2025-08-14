m=n=l=0
for _ in[0]*int(input()):
    o,*k=map(int,input().split())
    if o<2:
        l+=1
        if l>m:m=l;n=k[0]
        if l==m:n=min(n,k[0])
    else:l-=1
print(m,n)