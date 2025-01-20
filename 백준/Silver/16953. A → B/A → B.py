import collections as c
a,b=map(int,input().split())
q=c.deque([(a,1)])
while q:
    x,y=q.popleft()
    if x==b:print(y);break
    for i in (x*2,x*10+1):
        if i>b:continue
        q.append((i,y+1))
else:print(-1)