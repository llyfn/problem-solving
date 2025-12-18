for s in[*open(0)][1:]:
 n=int(s);a=0
 while n:m=n%100;a+=min(k+(m-25*k)//10+(m-25*k)%10for k in range(m//25+1));n//=100
 print(a)