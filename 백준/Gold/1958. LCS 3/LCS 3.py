a,b,c=input(),input(),input()
l=[[[0]*(len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        for k in range(1,len(c)+1):
            if a[i-1]==b[j-1]==c[k-1]:l[i][j][k]=l[i-1][j-1][k-1]+1
            else:l[i][j][k]=max(l[i-1][j][k],l[i][j-1][k],l[i][j][k-1])
print(l[-1][-1][-1])
