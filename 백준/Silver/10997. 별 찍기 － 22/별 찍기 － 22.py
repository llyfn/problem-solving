p=print;q='* ';r=' *';s='*';k=1
for i in range(n:=int(input())):
    if n<2:p(s);break
    if i<1:p(q*i+s*(4*(n-i)-3))
    elif i<2:p(q*i+s*(4*(n-i)-1))
    else: p(q*i+s*(4*(n-i)-1)+r*k);k+=1
    if i<1:p(s)
    elif i>n-2:p(s+r*(2*n-2))
    else:p(q*(i+1)+' '*(4*(n-i)-5)+r*i)
if n>1:p(s+r*(2*n-2))
for i in range(n-1,0,-1):
    p(q*i+' '*(4*(n-i)-3)+r*i)
    p(q*(i-1)+s*(4*(n-i)+1)+r
      *(i-1))