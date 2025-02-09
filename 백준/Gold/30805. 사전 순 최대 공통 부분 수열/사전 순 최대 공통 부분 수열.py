I=lambda:[*map(int,input().split())]
I();a=I();I();b=I();r=[]
while i:=set(a)&set(b):r+=(m:=max(i)),;a=a[a.index(m)+1:];b=b[b.index(m)+1:]
print(len(r));print(*r)