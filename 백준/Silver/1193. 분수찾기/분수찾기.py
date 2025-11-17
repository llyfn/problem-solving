X=int(input())
k=int((8*X-7)**.5+1)//2
p=X-k*(k-1)//2
print("%d/%d"%(p,k+1-p)[::1-k%2*2])