class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        se, sw = [[0] * (n + 2) for _ in range(m + 1)], [[0] * (n + 2) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                se[i][j] = se[i - 1][j - 1] + grid[i - 1][j - 1]
                sw[i][j] = sw[i - 1][j + 1] + grid[i - 1][j - 1]
        ans = []
        for i in range(m):
            for j in range(n):
                heappush(ans, grid[i][j])
                for k in range(i + 2, m, 2):
                    ux, uy, dx, dy = i, j, k, j
                    lx, ly, rx, ry = (i + k) // 2, j - (k - i) // 2, (i + k) // 2, j + (k - i) // 2
                    if ly < 0 or ry >= n: break
                    heappush(ans, sw[lx + 1][ly + 1] - sw[ux][uy + 2] + se[rx + 1][ry + 1] - se[ux][uy] + se[dx + 1][dy + 1] - se[lx][ly] + sw[dx + 1][dy + 1] - sw[rx][ry + 2] - grid[ux][uy] - grid[dx][dy] - grid[lx][ly] - grid[rx][ry])
                while len(ans) > 3: heappop(ans)
        return sorted(set(ans))[::-1]