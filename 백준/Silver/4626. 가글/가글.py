for k in range(int(input())):
    N,d,b,e=map(int,input().split())
    n=N%d
    o=''
    for i in range(e+1):
        n=n*7
        if i>=b:o+=str(n//d)
        n=n%d
    print(f'Problem set {k+1}: {N} / {d}, base 7 digits {b} through {e}: {o}')