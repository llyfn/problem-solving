input()
s=[*map(int,input().split())]
a=b=c=r=m=0
for i in s:
    m=max(m,c)
    if i==a:a=b;b=i;c+=1;r=1
    elif i==b:c+=1;r+=1
    else:a=b;b=i;c=r+1;r=1
print(max(m,c))