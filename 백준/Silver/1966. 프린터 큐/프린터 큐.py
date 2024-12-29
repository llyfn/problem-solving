from collections import deque

def printerQueue(n, m, arr):
    cnt = 0
    while m >= 0:
        if arr[0] == max(arr):
            arr.popleft()
            cnt += 1
            m -= 1
        else:
            arr.append(arr.popleft())
            if m == 0:
                m = len(arr) - 1
            else:
                m -= 1
    return cnt

ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    ans.append(printerQueue(n, m, arr))
for i in ans:
    print(i)
