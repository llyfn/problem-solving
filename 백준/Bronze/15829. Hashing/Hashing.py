input(); l = [ord(i) - ord('a') + 1 for i in input()]
print(sum(l[i] * 31 ** i for i in range(len(l))) % 1234567891)