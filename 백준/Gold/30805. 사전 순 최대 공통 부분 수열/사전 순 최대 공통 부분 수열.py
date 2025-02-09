I=lambda:[*map(int,input().split())]
I();a=I();I();b=I()
r=[]
while 1:
    while a and b:
        i=max(a);j=max(b);k=a.index(i);l=b.index(j)
        if i==j:break
        elif i>j:a.pop(k)
        else:b.pop(l)
    else:break
    r+=i,;a=a[k+1:];b=b[l+1:]
print(len(r))
if r:print(*r)