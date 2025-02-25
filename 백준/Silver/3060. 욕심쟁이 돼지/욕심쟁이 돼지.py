for _ in range(int(input())):
    n=int(input())
    s=sum(map(int,input().split()))
    for i in range(20):
        if s*4**i>n:print(i+1);break