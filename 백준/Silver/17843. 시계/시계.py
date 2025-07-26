for _ in[0]*int(input()):
    h,m,s=map(int,input().split())
    m+=s/60;h+=m/60;s*=6;m*=6;h*=30
    d=[*map(abs,[h-m,h-s,m-s])]
    print(min([*d,*[360-x for x in d]]))
