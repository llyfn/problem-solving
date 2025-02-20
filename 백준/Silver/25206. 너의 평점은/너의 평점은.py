g=[k for _ in[0]*20if(k:=input().split())[2]!='P']
S=C=0
for a,b,c in g:S+=(k:=float(b));C+=([4,3,2,1,0,0][ord(c[0])-65]+(c[-1]=='+')/2)*k
print(C/S)