R=range
M=10001
P=[*R(M)]
for i in R(2,M):
    if P[i]==i:P[i::i]=[x-x//i for x in P[i::i]]
for i in R(2,M):P[i]+=P[i-1]
for n in[*open(0)][1:]:print(P[int(n)]+1)