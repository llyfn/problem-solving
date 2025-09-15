n,x,*h=map(int,open(0).read().split())
m=min((a:=h[k-1],b:=h[k],e:=h[k+1],min(max(0,max(a+x-b,e+x-b)),(f:=max(0,a+x-b))+max(0,b+f+x-e),(f:=max(0,e+x-b))+max(0,b+f+x-a),max(0,b+x-a)+max(0,b+x-e)))[3]if 0<k<n-1else max(0,x-abs(h[k]-h[1-3*(k>0)]))for k in range(n))
print(m)