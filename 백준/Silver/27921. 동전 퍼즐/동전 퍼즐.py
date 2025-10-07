x,*l=open(0)
h,w=map(int,x.split())
a,b=l[:h],l[h+1:]
H,W=map(int,l[h].split())
o=[(i,j)for i in range(h)for j in range(w)if'.'<a[i][j]]
print(len(o)-max(sum(0<=i+y<H and 0<=j+x<W and'.'<b[i+y][j+x]for i,j in o)for y in range(-h,H)for x in range(-w,W)))