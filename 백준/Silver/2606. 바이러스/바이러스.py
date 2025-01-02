_, _, *graph = map(str.split, open(0))
c = {'1'}
found = True
while found:
    found = False
    for i in graph:
        if i[0] in c or i[1] in c:
            c.add(i[0])
            c.add(i[1])
            graph.remove(i)
            found = True
print(len(c) - 1)