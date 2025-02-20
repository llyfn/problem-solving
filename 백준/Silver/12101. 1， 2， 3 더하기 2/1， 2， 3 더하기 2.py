n,k=map(int,input().split())
r=[]
def f(x):
    if (s:=sum(x))>n:return
    if s==n:r.append(x)
    for i in (1,2,3):f(x+[i])
f([])
print('+'.join(map(str,r[k-1]))if k<=len(r)else-1)