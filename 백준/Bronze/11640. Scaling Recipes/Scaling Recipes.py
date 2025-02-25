for i in range(int(input())):
    r,p,d=map(int,input().split())
    l=[]
    for _ in range(r):
        I,W,P=input().split()
        if P=='100.0':k=float(W)/100*d/p
        l+=(I,float(P)),
    print(f'Recipe # {i+1}')
    for I,W in l:print(I,W*k)
    print('-'*40)