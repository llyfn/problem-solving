_,*h=open(0).readlines()
c={}
for e in h:
    t,n=e.split()
    c[n]=c.get(n,0)+int(t[:2])*60+int(t[3:])
for n in c:c[n]=max(0,c[n]-51)//50*3+10
for n in sorted(c,key=lambda x:(-c[x],x)):print(n,c[n])