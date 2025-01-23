I=lambda:map(int,input().split())
n,=I()
a=[*I()]
i,j=0,n-1
m,k,l=2e9,0,0
while i<j:
    x,y=a[i],a[j]
    if abs(x+y)<abs(m):m,k,l=x+y,x,y
    if x+y<0:i+=1
    else:j-=1
print(k,l)