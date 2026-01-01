import math
*I,=map(int,open(0).read().split())
n,k=I[:2]
X,Y=I[-2:]
A=sorted(math.atan2(y-Y,x-X)for x,y in zip(I[2:-2:2],I[3:-2:2]))
B=[a==b for a,b in zip(A,A[-1:]+A)]
print('YNEOS'[n%k>0 or all(any(B[i::n//k])for i in range(n//k))::2])