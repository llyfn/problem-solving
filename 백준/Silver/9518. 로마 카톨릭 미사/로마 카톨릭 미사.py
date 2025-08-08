r,s=map(int,input().split())
a=[[*input()]for _ in[0]*r]
d=-0,1,-1
d=[(i,j)for i in d for j in d][1:]
n=m=0
for x in range(r):
    for y in range(s):
        h=sum(0<=x+i<r and 0<=y+j<s and a[x+i][y+j]=='o'for i,j in d)
        if a[x][y]=='o':n+=h
        else:m=max(m,h)
print(n//2+m)