if (n := int(input())) in [3, 5]: print(1)
elif n in [4, 7]: print(-1)
else: r = n % 5; print((n // 5) + (r in [1, 3]) + 2 * (r in [2, 4]))