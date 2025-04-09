a,b,c,d,e,f,g,h=map(int,open(0).read().split())
F=lambda x,y,z,u,v,w:(w-y)*(z-x)-(u-y)*(v-x)
P,Q=F(a,b,c,d,e,f)*F(a,b,c,d,g,h),F(e,f,g,h,a,b)*F(e,f,g,h,c,d)
C=min(a,c)<=max(e,g)and min(e,g)<=max(a,c)and min(b,d)<=max(f,h)and min(f,h)<=max(b,d)if P==Q==0else P<=0and Q<=0
print(+C)
p=(a-c)*(f-h)-(b-d)*(e-g)
q=(a*d-b*c)*(e-g)-(a-c)*(e*h-f*g)
r=(a*d-b*c)*(f-h)-(b-d)*(e*h-f*g)
if C:
    if p==0:
        if (a,b)>(c,d):a,b,c,d=c,d,a,b
        if (e,f)>(g,h):e,f,g,h=g,h,e,f
        if (a,b)==(g,h)and (c,d)>(e,f):print(a,b)
        elif (c,d)==(e,f)and (a,b)<(g,h):print(c,d)
    else:print(q/p,r/p)