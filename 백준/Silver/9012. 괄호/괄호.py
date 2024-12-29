def validateVPS(x):
    parLv = 0
    for i in range(len(x)):
        if parLv < 0:
            return False

        if x[i] == '(':
            parLv += 1
        elif x[i] == ')':
            parLv -= 1
        else:
            return False
    return True if parLv == 0 else False

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
for i in range(n):
    if validateVPS(arr[i]):
        print("YES")
    else:
        print("NO")