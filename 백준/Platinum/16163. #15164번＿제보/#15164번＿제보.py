s=f'#{"#".join(input())}#'
n=len(s)
p=[0]*n
r=c=a=0
for i in range(n):
    if i<=r:p[i]=min(p[2*c-i],r-i)
    while i-p[i]>0and i+p[i]+1<n and s[i-p[i]-1]==s[i+p[i]+1]:p[i]+=1
    if i+p[i]>r:r=i+p[i];c=i
    a+=(p[i]+1)//2
print(a)