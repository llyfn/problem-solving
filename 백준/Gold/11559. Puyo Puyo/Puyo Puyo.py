from collections import deque

W, H = 6, 12
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

map = [list(input().strip()) for _ in range(H)]

def Blast(x, y, check):
    q = deque()
    q.append([x, y])
    vstd = [[0] * W for _ in range(H)]
    vstd[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and map[nx][ny] == map[x][y] and vstd[nx][ny] == 0:
                q.append([nx, ny])
                vstd[nx][ny] = 1
                cnt += 1
                
    if cnt >= 4:
        check += 1
        for h in range(H):
            for w in range(W):
                if vstd[h][w]:
                    map[h][w] = '.'

    return check

def Fall():
    for h in reversed(range(H-1)):
        for w in range(W):
            if map[h][w] != '.' and map[h+1][w] == '.':
                for k in range(h+1, H):
                    if k == H-1 and map[k][w] == '.':
                        map[k][w] = map[h][w]
                    elif map[k][w] != '.':
                        map[k-1][w] = map[h][w]
                        break
                map[h][w] = '.'
            
ans = 0
checkBlast = 1
while checkBlast != 0:
    checkBlast = 0
    for h in range(H):
        for w in range(W):
            if map[h][w] != '.':
                checkBlast = Blast(h, w, checkBlast)
    if checkBlast != 0:
        ans += 1
    Fall()
print(ans)