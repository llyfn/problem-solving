n = int(input())
tower = list(map(int, input().split()))
stack = []
goto = [0] * n
for i in range(n):
    t = tower[i]
    while stack and tower[stack[-1]] < t:
        stack.pop()
    if stack:
        goto[i] = stack[-1] + 1
    stack.append(i)
            
print(' '.join(list(map(str, goto))))