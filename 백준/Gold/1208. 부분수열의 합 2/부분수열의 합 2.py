(n,s),l=[[*map(int,s.split())]for s in open(0)]
def f(x,y):
    if x<n//2:f(x+1,y+l[x]);f(x+1,y)
    elif y in p:p[y]+=1
    else:p[y]=1
def g(x,y):
    if x<n:g(x+1,y+l[x]);g(x+1,y)
    elif s-y in p:global r;r+=p[s-y]
p={}
r=0
f(0,0)
g(n//2,0)
print(r-(not s))