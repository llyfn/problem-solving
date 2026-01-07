x=X=y=Y=r=c=0;I=iter(open(0).read().split());next(I)
for k,s in zip(I,I):p=0;P=[0]+[p:=p+1j**"ENWS".find(d)for d in s];f=int(k)-1;g,h=p.real,p.imag;A=f*g;B=f*h;u,v=min(S:={z.real for z in P}),max(S);w,z=min(T:={z.imag for z in P}),max(T);x=min(x,r+u,r+u+A);X=max(X,r+v,r+v+A);y=min(y,c+w,c+w+B);Y=max(Y,c+z,c+z+B);r+=A+g;c+=B+h
print(int(Y-y),int(X-x))