p=print
a=lambda x:p('* '*(x-1)+'*'*(4*(n-x)+1)+' *'*(x-1))
b=lambda x:p('* '*x+' '*(4*(n-x)-3)+' *'*x)
for i in range(1,n:=int(input())):a(i);b(i)
p('* '*(2*n-1))
for i in range(n-1,0,-1):b(i);a(i)