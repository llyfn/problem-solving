I=lambda:map(int,input().split())
n,=I()
d=[0,0]
for _ in range(n):
    l=[*I()]
    d=[0,*[l[i]+max(d[i],d[i+1])for i in range(len(l))],0]
print(max(d))
