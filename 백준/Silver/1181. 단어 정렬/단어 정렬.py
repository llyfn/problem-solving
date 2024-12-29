l = [*set([input() for _ in range(int(input()))])]
l.sort(key=lambda x: (len(x), x))
print('\n'.join(l))
