_,*l=open(0)
for s in l:
    r,b,m=map(float,s.split())
    for i in range(1200):
        b=int(b*(r+100)+.5)/100-m
        if b<=0:print(i+1);break
    else:print("impossible")