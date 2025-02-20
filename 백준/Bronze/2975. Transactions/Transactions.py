for s in open(0):
    a,b,c=s.split()
    if c=='0':break
    i=int(a)+int(c)*(1-2*(b=='W'))
    print([i,'Not allowed'][i<-200])