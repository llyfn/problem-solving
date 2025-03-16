I=lambda:input().split()
n,m,k=map(int,I())
s={}
r=0
for i in[0]*n:a,b=I();s[a]=int(b)
for i in[0]*k:a,=I();r+=s[a];del s[a]
s=sorted(s.values())
p=q=0
for i in range(m-k):p+=s[i];q+=s[-i-1]
print(r+p,r+q)