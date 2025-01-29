m=int(input())
M=1000000007
a=0
for _ in[0]*m:n,s=map(int,input().split());a=(a+s*pow(n,M-2,M))%M
print(a)