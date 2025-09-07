I=lambda:[*map(int,input().split())]
for _ in[0]*I()[0]:
 c,v=I();p=[I()for _ in[0]*v];f={};s={}
 for i in p:f[i[0]]=f.get(i[0],0)+1
 for i,j in f.items():
  if j>v//2:print(i,1);break
 else:t=sorted(f.items(),key=lambda x:x[1])[-2:];[s.update({(k:=min(t,key=lambda x:i.index(x[0]))[0]):s.get(k,0)+1})for i in p];print(max(s,key=s.get),2)