while (i:=input())!='#':k=lambda x:i.count(x);l=len(i);print("need quorum"if k('A')>=l/2 else'yes'if k('Y')>k('N')else'no'if k('N')>k('Y')else'tie')