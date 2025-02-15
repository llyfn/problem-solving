s,a=[],''
p=lambda i,j:2 if i in'+-'else 1 if i in'*/'else j*3
for i in input():
    if ord(i)>47:a+=i
    elif i==')':
        while s[-1]!='(':a+=s.pop()
        s.pop()
    else:
        while s and p(i,0)>=p(s[-1],1):a+=s.pop()
        s+=i,
while s:a+=s.pop()
print(a)