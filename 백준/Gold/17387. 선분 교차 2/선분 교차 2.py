a,b,c,d,e,f,g,h=map(int,open(0).read().split())
F=lambda x,y,z,u,v,w:(w-y)*(z-x)-(u-y)*(v-x)
P,Q=F(a,b,c,d,e,f)*F(a,b,c,d,g,h),F(e,f,g,h,a,b)*F(e,f,g,h,c,d)
print(+(min(a,c)<=max(e,g)and min(e,g)<=max(a,c)and min(b,d)<=max(f,h)and min(f,h)<=max(b,d))if P==Q==0else+(P<=0and Q<=0))