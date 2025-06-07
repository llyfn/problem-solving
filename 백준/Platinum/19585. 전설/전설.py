import sys

input = sys.stdin.readline

def check(word):
    curr = colors
    for i in range(len(word)):
        if curr.get(0) and word[i:] in names:
            return 1
        if not curr.get(word[i]):
            return
        curr = curr[word[i]]

c, n = map(int, input().split())
colors = dict()
for _ in range(c):
    curr = colors
    for ch in input().strip():
        if ch not in curr:
            curr[ch] = dict()
        curr = curr[ch]
    curr[0] = 1
names = { input().strip() for _ in range(n) }
for _ in range(int(input())): print('Yes' if check(input().strip()) else 'No')