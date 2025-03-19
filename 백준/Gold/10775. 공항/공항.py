G,P,*g=map(int,open(0).read().split())
s=[*range(G+1)]
r=0
def f(x):
    if s[x]!=x:s[x]=f(s[x])
    return s[x]
def u(x,y):s[x]=f(y)
for i in g:
    if f(i)<1:break
    r+=1;u(f(i),f(i)-1)
print(r)