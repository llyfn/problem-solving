n=int(input())
s=[*map(int,input().split())]
a=b=c=r=i=m=0
for i in range(n):
    m=max(m,c)
    if s[i]==a:a=b;b=s[i];c+=1;r=1
    elif s[i]==b:c+=1;r+=1
    else:a=b;b=s[i];c=r+1;r=1
print(max(m,c))