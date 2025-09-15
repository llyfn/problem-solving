n,x,*h=map(int,open(0).read().split())
h=[9**9,*h,9**9]
m=min((a:=h[k],b:=h[k+1],e:=h[k+2],min(max(0,max(a+x-b,e+x-b)),(f:=max(0,a+x-b))+max(0,b+f+x-e),(f:=max(0,e+x-b))+max(0,b+f+x-a),max(0,b+x-a)+max(0,b+x-e)))[3]for k in range(n))
print(m)