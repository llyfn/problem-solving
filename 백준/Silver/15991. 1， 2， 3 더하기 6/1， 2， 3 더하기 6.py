K=100001
d=[1,1,2,2,3,3]+[0]*K
for i in range(6,K):d[i]=sum(d[i-6:i:2])%(10**9+9)
for i in[*open(0)][1:]:print(d[int(i)])