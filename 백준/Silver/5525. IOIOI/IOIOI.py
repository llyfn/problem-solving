n,m,s=int(input()),int(input()),input()
a=c=i=0
while i<m-1:
    if s[i:i+3] == 'IOI':
        c+=1;i+=2
        if c==n:a+=1;c-=1
    else: i += 1;c=0
print(a)