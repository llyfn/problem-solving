import sys
input = sys.stdin.readline

sys.setrecursionlimit(300000)
N = int(input())

adj = [[] for _ in range(N + 1)]
edges = []

for i in range(N - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, i))
    adj[v].append((u, i))
    edges.append((u, v, w))

parent = [0] * (N + 1)
depth = [0] * (N + 1)
subtree_size = [1] * (N + 1)
heavy = [-1] * (N + 1)

order = []
visited = [False] * (N + 1)
stack = [(1, 0, False)]
while stack:
    node, par, processed = stack.pop()
    if processed:
        max_size = 0
        for nxt, _ in adj[node]:
            if nxt == par:
                continue
            subtree_size[node] += subtree_size[nxt]
            if subtree_size[nxt] > max_size:
                max_size = subtree_size[nxt]
                heavy[node] = nxt
    else:
        visited[node] = True
        parent[node] = par
        order.append(node)
        stack.append((node, par, True))
        for nxt, _ in adj[node]:
            if not visited[nxt]:
                depth[nxt] = depth[node] + 1
                stack.append((nxt, node, False))

head = [0] * (N + 1)
pos = [0] * (N + 1)
cur_pos = [0]

stack2 = [(1, 1)]
while stack2:
    node, h = stack2.pop()
    head[node] = h
    pos[node] = cur_pos[0]
    cur_pos[0] += 1
    for nxt, _ in adj[node]:
        if nxt == parent[node] or nxt == heavy[node]:
            continue
        stack2.append((nxt, nxt))
    if heavy[node] != -1:
        stack2.append((heavy[node], h))

size = N
seg = [0] * (4 * size)

def update(node, start, end, idx, val):
    if start == end:
        seg[node] = val
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(2*node, start, mid, idx, val)
    else:
        update(2*node+1, mid+1, end, idx, val)
    seg[node] = max(seg[2*node], seg[2*node+1])

def query(node, start, end, l, r):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return seg[node]
    mid = (start + end) // 2
    return max(query(2*node, start, mid, l, r), query(2*node+1, mid+1, end, l, r))

edge_node = []
for i, (u, v, w) in enumerate(edges):
    deeper = v if depth[v] > depth[u] else u
    edge_node.append(deeper)
    update(1, 0, N-1, pos[deeper], w)

def path_max(u, v):
    res = 0
    while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u
        res = max(res, query(1, 0, N-1, pos[head[u]], pos[u]))
        u = parent[head[u]]
    if u == v:
        return res
    if depth[u] > depth[v]:
        u, v = v, u
    res = max(res, query(1, 0, N-1, pos[u]+1, pos[v]))
    return res

M = int(input())
out = []
for _ in range(M):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i, c = q[1] - 1, q[2]
        node = edge_node[i]
        update(1, 0, N-1, pos[node], c)
    else:
        u, v = q[1], q[2]
        out.append(path_max(u, v))

print('\n'.join(map(str, out)))