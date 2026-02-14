tc = 0
while True:
    tc += 1
    E = input()
    if E == "()": break
    max_d = d = 0
    for c in E:
        if c == "(": d += 1; max_d = max(d, max_d)
        elif c == ")": d -= 1;
    stack = [(max_d - d) % 2 == 0]
    for c in E:
        if c == "(": d += 1; stack.append((max_d - d) % 2 == 0)
        else:
            if c == ")": d -= 1; val = stack.pop()
            else: val = (c == "T")
            if (max_d - d) % 2 == 0: stack[-1] &= val
            else: stack[-1] |= val
    print(f'{tc}. {"true" if stack[0] else "false"}')
