a,b,c=map(int,input().split())
a=round((((a*a-b*b)*(a*a-c*c))**.5-b*c)/a)
print(-1*(a<0)or a)