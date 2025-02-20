input();a=[*map(int,input().split())];s=0
print(sum(a[i+1]*(s:=s+a[i])for i in range(len(a)-1)))