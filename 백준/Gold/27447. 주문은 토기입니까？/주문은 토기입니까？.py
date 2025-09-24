n,m,*t=map(int,open(0).read().split())
k=l=n-1
p=0
for i in range(t[-1],-1,-1):
    if l<0:
        if p:p-=1
        else:break
    elif i==t[k]:p+=1;k-=1
    elif t[l]>i+m:break
    elif t[l]>i:l-=1
    else:p-=p>0
print("fail"if p else"success")