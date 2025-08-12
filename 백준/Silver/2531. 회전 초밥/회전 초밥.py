n,d,k,c,*s=map(int,open(0).read().split())
t=[0]*(d+1)
a=0
for i in s[:k]:t[i]+=1
a=sum(t[i]>0for i in range(d+1))+(t[c]<1)
for i in range(n):
    t[s[i]]-=1
    t[s[(i+k)%n]]+=1
    a=max(a,sum(t[i]>0for i in range(d+1))+(t[c]<1))
print(a)