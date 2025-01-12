import sys, collections as c
I=lambda:sys.stdin.readline().strip()
for _ in range(int(I())):
    p=I()
    n=int(I())
    x=c.deque(eval(I()))
    r=1
    for o in p:
        if o=='R':r^=1
        elif x:x.popleft() if r else x.pop()
        else:print('error');break
    else: print('['+','.join([*map(str,x)][::1 if r else -1])+']')
