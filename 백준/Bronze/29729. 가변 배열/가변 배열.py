s,n,m=map(int,input().split())
l=0
for _ in range(n+m):
    if input()=='1':
        if l<s:l+=1
        else:s*=2;l+=1
    else:l-=1
print(s)