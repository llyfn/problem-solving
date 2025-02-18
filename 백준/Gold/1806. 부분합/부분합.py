I=lambda:map(int,input().split())
n,s=I()
a=[*I()]
l,r,m,S=0,0,1e9,0
while 1:
    if S>=s:m=min(m,r-l);S-=a[l];l+=1
    elif r==n:break
    else:S+=a[r];r+=1
print([0,m][m<1e9])