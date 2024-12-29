s = list(map(int, input().split()))
print('ascending' if s == sorted(s) else 'descending' if s == sorted(s, reverse=True) else 'mixed')