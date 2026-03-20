class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                s = sorted({grid[r][c] for r in range(i, i+k) for c in range(j, j+k)})
                row.append(min((s[x+1] - s[x] for x in range(len(s)-1)), default=0))
            res.append(row)
        return res
