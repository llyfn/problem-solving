from collections import deque

def validateParen(s):
    q = deque()
    value = 0
    temp = 1

    for i in range(len(s)):
        if s[i] == '(':
            q.append(s[i])
            temp *= 2

        elif s[i] == '[':
            q.append(s[i])
            temp *= 3

        elif s[i] == ')':
            if not q:
                return 0
            x = q.pop()
            if x == '[':
                return 0
            if s[i-1] == '(':
                value += temp
            temp //= 2

        elif s[i] == ']':
            if not q:
                return 0
            x = q.pop()
            if x == '(':
                return 0
            if s[i-1] == '[':
                value += temp
            temp //= 3

        else:
            return 0

    if q:
        return 0
    return value

print(validateParen(input()))