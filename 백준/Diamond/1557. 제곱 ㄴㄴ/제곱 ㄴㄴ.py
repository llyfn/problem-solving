K=10**6
M,k,l,r=[0]*K,int(input()),0,2<<32
M[1]=1
for i in range(1,K):
    for j in range(2*i,K,i):M[j]-=M[i]
def f(n):
    a,b=1,0
    while a*a<=n:b+=M[a]*(n//a**2);a+=1
    return b
while l<r-1:
    m=(l+r)//2
    if f(m)<k:l=m
    else:r=m
print(r)