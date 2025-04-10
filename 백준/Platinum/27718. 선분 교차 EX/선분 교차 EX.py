I=lambda:[*map(int,input().split())]
N,=I()
L=[]
A=[N*[3]for _ in[0]*N]
F=lambda x,y,z,u,v,w:(w-y)*(z-x)-(u-y)*(v-x)
for i in range(N):
    a,b,c,d=I()
    if (a,b)>(c,d):a,b,c,d=c,d,a,b
    for j,(e,f,g,h)in enumerate(L):
        P,Q=F(a,b,c,d,e,f)*F(a,b,c,d,g,h),F(e,f,g,h,a,b)*F(e,f,g,h,c,d)
        p=(a-c)*(f-h)-(b-d)*(e-g)
        q=(a*d-b*c)*(e-g)-(a-c)*(e*h-f*g)
        r=(a*d-b*c)*(f-h)-(b-d)*(e*h-f*g)
        if a<=g and e<=c and min(b,d)<=max(f,h)and min(f,h)<=max(b,d)if P==Q==0else P<=0and Q<=0:
            if(a-c)*(f-h)-(b-d)*(e-g)==0:
                if (a,b)==(g,h)and(c,d)>(e,f)or(c,d)==(e,f)and(a,b)<(g,h):A[i][j]=A[j][i]=1
            else:A[i][j]=A[j][i]=2-((q/p,r/p)in[(a,b),(c,d),(e,f),(g,h)])
        else:A[i][j]=A[j][i]=0
    L+=(a,b,c,d),
for i in A:print(*i,sep='')