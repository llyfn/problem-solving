t=0;l=1;M=10**9+9
for i in input():
    if i=='c':l=l*(26-(i==t))%M
    else:l=l*(10-(i==t))%M
    t=i
print(l)