I=lambda:[*map(int,input().split())]
for _ in range(*I()):
    I();a=b=c=d=0
    for p,q in zip(I(),I()):x=p+max(b,c,d);y=q+max(a,c,d);c=a;d=b;a=x;b=y
    print(max(a,b))
