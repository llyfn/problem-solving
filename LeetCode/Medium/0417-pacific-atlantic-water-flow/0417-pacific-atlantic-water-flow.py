class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        pv = [[0] * n for _ in range(m)]
        av = [[0] * n for _ in range(m)]
        def bfs(i, j, v):
            if v[i][j]: return
            v[i][j] = 1
            q = [(i, j)]
            while q:
                i, j = q.pop(0)
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and v[ni][nj] == 0 and heights[ni][nj] >= heights[i][j]:
                        q.append((ni, nj))
                        v[ni][nj] = 1
        for i in range(m):
            bfs(i, 0, pv)
            bfs(i, n - 1, av)
        for i in range(n):
            bfs(0, i, pv)
            bfs(m - 1, i, av)
        return [[i, j] for i in range(m) for j in range(n) if pv[i][j] and av[i][j]]