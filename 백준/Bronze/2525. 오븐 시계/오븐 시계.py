a,b,c=map(int,open(0).read().split())
c+=b+a*60
print(c//60%24,c%60)