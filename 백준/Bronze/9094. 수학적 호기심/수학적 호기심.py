for _ in[0]*int(input()):
    n,m=map(int,input().split())
    print(sum((i*i+j*j+m)%(i*j)==0for i in range(1,n)for j in range(i+1,n)))