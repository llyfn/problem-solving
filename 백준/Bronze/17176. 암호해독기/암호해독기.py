n=int(input())
c=[*map(int,input().split())]
s=input()
l=[]
for i in s:l+=ord(i)*i.isalpha()-70*i.islower()-64*i.isupper(),
print("ny"[sorted(l)==sorted(c)])