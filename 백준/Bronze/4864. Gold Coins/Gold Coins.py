for s in open(0):
    if i:=int(s):k=int(-.5+(8*i+1)**.5/2);print(i,sum(i**2 for i in range(k+1))+(k+1)*(i-k*(k+1)//2))