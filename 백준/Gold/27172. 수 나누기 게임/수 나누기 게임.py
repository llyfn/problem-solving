_,l=open(0)
l=set(map(int,l.split()))
m=max(l)+1
s=[0]*m
for i in l:
    for j in range(2*i,m,i):
        if j in l:s[i]+=1;s[j]-=1
print(*[s[i] for i in l])