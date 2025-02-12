a,b=0,1
for _ in range(int(input())%(15*10**5)):a,b=b,(a+b)%10**6
print(a)