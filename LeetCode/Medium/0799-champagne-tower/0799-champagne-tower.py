class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        g = [[0] * 100 for _ in range(100)]
        g[0][0] = poured
        for r in range(0, query_row):
            for c in range(0, r + 1):
                if g[r][c] > 1:
                    v = (g[r][c] - 1) / 2
                    g[r + 1][c] += v
                    g[r + 1][c + 1] += v
        return min(1, g[query_row][query_glass])