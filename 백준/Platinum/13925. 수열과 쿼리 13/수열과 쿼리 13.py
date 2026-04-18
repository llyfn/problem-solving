import sys
input = sys.stdin.readline
MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))
m = int(input())
size = 1
while size < n: size <<= 1
tree = [0] * (2 * size)
lazy_mul = [1] * (2 * size)
lazy_add = [0] * (2 * size)
for i in range(n): tree[size + i] = a[i] % MOD
for i in range(size - 1, 0, -1): tree[i] = (tree[2*i] + tree[2*i+1]) % MOD
def apply_node(node, length, mul, add):
    tree[node] = (mul * tree[node] + add * length) % MOD
    lazy_mul[node] = lazy_mul[node] * mul % MOD
    lazy_add[node] = (lazy_add[node] * mul + add) % MOD
def push_down(node, length):
    if lazy_mul[node] != 1 or lazy_add[node] != 0:
        half = length >> 1
        apply_node(2*node,   half, lazy_mul[node], lazy_add[node])
        apply_node(2*node+1, half, lazy_mul[node], lazy_add[node])
        lazy_mul[node] = 1
        lazy_add[node] = 0
def update(node, node_l, node_r, l, r, mul, add):
    if r < node_l or node_r < l: return
    if l <= node_l and node_r <= r:
        apply_node(node, node_r - node_l + 1, mul, add)
        return
    push_down(node, node_r - node_l + 1)
    mid = (node_l + node_r) >> 1
    update(2*node,   node_l, mid,    l, r, mul, add)
    update(2*node+1, mid+1,  node_r, l, r, mul, add)
    tree[node] = (tree[2*node] + tree[2*node+1]) % MOD
def query(node, node_l, node_r, l, r):
    if r < node_l or node_r < l: return 0
    if l <= node_l and node_r <= r: return tree[node]
    push_down(node, node_r - node_l + 1)
    mid = (node_l + node_r) >> 1
    return (query(2*node, node_l, mid, l, r) + query(2*node+1, mid+1, node_r, l, r)) % MOD
sys.setrecursionlimit(300000)
out = []
for _ in range(m):
    line = sys.stdin.readline().split()
    t = int(line[0])
    x, y = int(line[1]) - 1, int(line[2]) - 1
    if t == 1:
        v = int(line[3]) % MOD
        update(1, 0, size-1, x, y, 1, v)
    elif t == 2:
        v = int(line[3]) % MOD
        update(1, 0, size-1, x, y, v, 0)
    elif t == 3:
        v = int(line[3]) % MOD
        update(1, 0, size-1, x, y, 0, v)
    else:
        out.append(query(1, 0, size-1, x, y))
print('\n'.join(map(str, out)))