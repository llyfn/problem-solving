import sys
I=lambda:[*map(int,sys.stdin.readline().split())]
N,Q=I()
A=sorted(I())
for i in range(1,N):A[i]+=A[i-1]
for _ in[0]*Q:l,r=I();print(A[r-1]-(l>1)*A[l-2])