f=lambda s,p:(not s)or sum(f(s[i:],n)for i in range(1,len(s)+1)if(n:=int(s[:i],16))>=p)
for i in open(0).read().split()[1:]:print(f(i,0))