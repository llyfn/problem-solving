s={'A': 4, 'B': 3, 'C': 2, 'D': 1}.get((i := input())[0], 0) + (0.3 if '+' in i[1:] else -0.3 if '-' in i[1:] else 0)
print(f'{s:.1f}')