import sys
I=lambda:map(int,sys.stdin.readline().split())
n,=I()
d=[[0]*3]
for _ in range(n):
    r,g,b=I()
    x,y,z=d[-1]
    d+=[r+min(y,z),g+min(x,z),b+min(x,y)],
print(min(d[-1]))