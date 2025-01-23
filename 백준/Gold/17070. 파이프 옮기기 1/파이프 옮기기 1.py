I=lambda:map(int,input().split())
n,=I()
m=[[*I()]for _ in range(n)]
d=[[[0]*3 for _ in range(n)]for _ in range(n)]
d[0][1][0]=1
for i in range(n):
    for j in range(1,n):
        x,y,z=0,0,0
        if m[i][j]<1 and (i,j)!=(0,1):
            x=d[i][j-1][0]+d[i][j-1][2]
            if i>0:
                y=d[i-1][j][1]+d[i-1][j][2]
                if m[i-1][j]<1 and m[i][j-1]<1:z=sum(d[i-1][j-1])
            d[i][j]=[x,y,z]
print(sum(d[-1][-1]))
