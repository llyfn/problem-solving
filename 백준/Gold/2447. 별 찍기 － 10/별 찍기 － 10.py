def f(n):
    if n<3:return['*']
    s=f(n//3)
    return[*[i*3 for i in s],*[i+' '*(n//3)+i for i in s],*[i*3 for i in s]]
print('\n'.join(f(int(input()))))