def knapsack(W, arr):
    val = [[0] * (W+1) for _ in range(len(arr)+1)]
    for i in range(len(arr)):
        val[i][0] = 0
    for w in range(W):
        val[0][w] = 0
    for i in range(1, len(arr)+1):
        for w in range(1, W+1):
            if arr[i-1][0] > w:
                val[i][w] = val[i-1][w]
            else:
                val[i][w] = max(val[i-1][w-arr[i-1][0]] + arr[i-1][1], val[i-1][w])

    return val[-1][-1]


N, K = map(int, input().strip().split())
arr = [tuple(map(int, input().strip().split())) for _ in range(N)]

print(knapsack(K, arr))