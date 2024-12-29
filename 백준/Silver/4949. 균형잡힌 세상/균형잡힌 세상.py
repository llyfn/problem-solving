import collections as c
while True:
    if (i := input()) == '.': break
    d = c.deque()
    for j in i:
        if j in '([':
            d.append(j)
        elif j in ')]':
            if not d or d[-1] != '[('['])'.index(j)]:
                print('no')
                break
            d.pop()
    else:
        print('yes' if not d else 'no')
