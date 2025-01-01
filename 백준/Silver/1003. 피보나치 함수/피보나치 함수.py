_,*l=open(0)
for i in l:
    x=1;y=0
    for j in range(int(i)):x,y=y,x+y
    print(x,y)