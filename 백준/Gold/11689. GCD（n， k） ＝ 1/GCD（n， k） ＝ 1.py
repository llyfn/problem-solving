n=m=int(input())
i=1
while 1:
    i+=1
    if i*i>n:break
    if n%i:continue
    m-=m/i
    while n%i==0:n//=i
if n>1:m-=m//n
print(int(m))