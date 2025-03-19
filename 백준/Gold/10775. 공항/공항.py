G,P,*g=map(int,open(0))
s=[*range(G+1)]
r=0
def f(x):
    if s[x]!=x:s[x]=f(s[x])
    return s[x]
for i in g:
    if(x:=f(i))<1:break
    r+=1;s[x]=f(x-1)
print(r)