n=int(input())
q=n//3
r=n%3
print(1+n+(n*n-3*q*q-2*r*q-r)//2)