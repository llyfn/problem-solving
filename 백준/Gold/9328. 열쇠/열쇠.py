from collections import deque
d=[(-1,0),(1,0),(0,-1),(0,1)]
def f(v):
    q=deque([(0,0)]);v[0][0]=1
    while q:
        r,c=q.popleft()
        for dx,dy in d:
            x,y=r+dx,c+dy
            if x<0 or x>=h+2or y<0 or y>=w+2or (z:=m[x][y])=='*'or v[x][y]:continue
            if '@'<z<'[':
                if z.lower()not in k:continue
            elif '`'<z<'{':
                if z not in k:k[z]=1;v=[[0]*(w+2)for _ in range(h+2)]
            elif z=="$"and(x,y)not in t:global a;a+=1;t.append((x,y))
            v[x][y]=1
            q.append((x,y))
for _ in[0]*int(input()):
    h,w=map(int,input().split())
    m=['.'*(w+2)]+[f'.{input()}.'for _ in[0]*h]+['.'*(w+2)]
    v=[[0]*(w+2)for _ in[0]*(h+2)]
    k={i:1for i in input()}
    t=[]
    a=0
    f(v)
    print(a)