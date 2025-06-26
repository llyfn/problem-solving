a,b,c,d,e,f=map(int,open(0).read().split())
x=a*d+c*f+e*b-b*c-d*e-f*a
print((x>0)-(x<0))