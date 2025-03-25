s=input()
R=range
n=len(s)
d=[2500]*(n+1)
d[-1]=0
p=[[0]*n for _ in R(n)]
p[0][0]=1
for i in R(1,n):p[i][i]=1;p[i-1][i]=+(s[i-1]==s[i])
for i in R(2,n):
    for l in R(n-i):p[l][r]=+(s[l]==s[r:=l+i] and p[l+1][r-1])
for r in R(n):
    for l in R(r+1):d[r]=min(d[r],d[l-1]+1if p[l][r]else d[r-1]+1)
print(d[-2])