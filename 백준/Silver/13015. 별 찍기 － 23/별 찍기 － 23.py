p=print;q='*';r=' '
n=int(input())
p(q*n+r*(2*n-3)+q*n)
for i in range(2,n):p(r*(i-1)+q+r*(n-2)+q+r*(2*(n-i)-1)+q+r*(n-2)+q)
p(r*(n-1)+q+r*(n-2)+q+r*(n-2)+q)
for i in range(n-1,1,-1):p(r*(i-1)+q+r*(n-2)+q+r*(2*(n-i)-1)+q+r*(n-2)+q)
p(q*n+r*(2*n-3)+q*n)