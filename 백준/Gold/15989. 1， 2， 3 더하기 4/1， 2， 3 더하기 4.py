m=10001
d=[1]*m
for i in range(2,m):d[i]+=d[i-2]
for i in range(3,m):d[i]+=d[i-3]
for i in[*open(0)][1:]:print(d[int(i)])