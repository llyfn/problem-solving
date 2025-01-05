import re
e = input()
f = lambda s: sum(map(int, re.split('\\+|-', s)))
if (i := e.find('-')) == -1: print(f(e))
else: print(f(e[:i]) - f(e[i+1:]))