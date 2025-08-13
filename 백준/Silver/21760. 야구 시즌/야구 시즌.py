for _ in[0]*int(input()):
    n,m,k,d=map(int,input().split())
    b=0
    x=n*m*(k*(m-1)+m*(n-1))
    while x*b<=2*d:b+=1
    if b<2:print(-1)
    else:print(x*(b-1)//2)