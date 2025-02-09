a,b=input(),input()
n,m=len(a),len(b)
l=[[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:l[i][j]=l[i-1][j-1]+1
        else:l[i][j]=max(l[i-1][j],l[i][j-1])
print(l[-1][-1])
s=''
while n>0 and m>0:
    if l[n][m]==l[n-1][m]:n-=1
    elif l[n][m]==l[n][m-1]:m-=1
    else:s+=a[n-1];n-=1;m-=1
print(s[::-1])