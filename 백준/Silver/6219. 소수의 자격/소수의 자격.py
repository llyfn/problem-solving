a,b,d=map(int,input().split())
print(len([n for n in range(a,b+1)if n>1and str(d)in str(n)and all(n%i for i in range(2,int(n**.5)+1))]))