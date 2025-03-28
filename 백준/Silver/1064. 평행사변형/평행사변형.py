a,b,c,d,e,f=map(int,input().split())
l=[(a-c)**2+(b-d)**2,(a-e)**2+(b-f)**2,(c-e)**2+(d-f)**2]
print(-1.0if(a-c)*(f-d)==(b-d)*(e-c)else(max(l)**0.5-min(l)**0.5)*2)