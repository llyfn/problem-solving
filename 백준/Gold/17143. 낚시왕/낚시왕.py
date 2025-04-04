f=lambda:map(int,input().split())
R,C,M=f()
S,P=[],[[0]*(C+1)for _ in[0]*(R+1)]
for _ in[0]*M:r,c,s,d,z=f();S+=[r,c,s%([R,C][d>2]*2-2),d-1,z,1],;P[r][c]=z
DY=[-1,1,0,0]
DX=[0,0,1,-1]
CD=[1,0,3,2]
A=0
for c in range(1,C+1):
    for y in range(1,R+1):
        if P[y][c]:
            A+=P[y][c]
            for s in S:
                if s[5]<1:continue
                if s[:2]==[y,c]:s[5]=0;break
            break
    P=[[0]*(C+1)for _ in[0]*(R+1)]
    for s in S:
        if s[-1]<1:continue
        y,x=s[:2]
        for _ in range(s[2]):
            y,x=s[0]+DY[s[3]],s[1]+DX[s[3]]
            if y>R or y<1 or x>C or x<1:s[3]=CD[s[3]];y,x=s[0]+DY[s[3]],s[1]+DX[s[3]]
            s[:2]=y,x
        if P[y][x]:
            if P[y][x]<s[4]:
                for t in S:
                    if t[5]and t[4]==P[y][x]:t[5]=0;break
                P[y][x]=s[4]
            else:s[5]=0
        else:P[y][x]=s[4]
print(A)