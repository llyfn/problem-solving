for l in[*open(0)][:-1]:
 x,y=map(int,l.split())
 d={x:0};c,s=x,0
 while c>1:c=(3*c+1,c//2)[c%2<1];s+=1;d[c]=s
 c,s=y,0
 while c not in d:c=(3*c+1,c//2)[c%2<1];s+=1
 print(f'{x} needs {d[c]} steps, {y} needs {s} steps, they meet at {c}')