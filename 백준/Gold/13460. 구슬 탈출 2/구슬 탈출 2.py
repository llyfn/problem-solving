N,M=map(int,input().split())
B=[]
for i in range(N):
    B+=(s:=input()),
    for j in range(M):
        if s[j]=='R':P,Q=i,j
        if s[j]=='B':R,S=i,j
D=[(0,1),(1,0),(0,-1),(-1,0)]
q=[(P,Q,R,S)];v=[(P,Q,R,S)];r=0
while q:
    for _ in[0]*len(q):
        a,b,c,d=q.pop(0)
        if r>10:print(-1);exit()
        if B[a][b]=='O':print(r);exit()
        for i in range(4):
            e,f,g,h=a,b,c,d;x,y=D[i]
            while 1:
                e+=x;f+=y
                if B[e][f]=='#':e-=x;f-=y;break
                if B[e][f]=='O':break
            while 1:
                g+=x;h+=y
                if B[g][h]=='#':g-=x;h-=y;break
                if B[g][h]=='O':break
            if B[g][h]=='O':continue
            if e==g and f==h:
                if abs(e-a)+abs(f-b)>abs(g-c)+abs(h-d):e-=x;f-=y
                else:g-=x;h-=y
            if (e,f,g,h)not in v:v+=[(e,f,g,h)];q+=[(e,f,g,h)]
    r+=1
print(-1)