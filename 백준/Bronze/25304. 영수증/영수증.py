I=lambda:map(int,input().split())
t,=I()
n,=I()
for _ in range(n):
    a,b=I()
    t-=a*b
print("YNeos"[t!=0::2])
