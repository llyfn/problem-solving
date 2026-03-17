class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        ans = 0
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val and r > 0: row[c] += matrix[r - 1][c]
            ans = max(ans, *[h * w for w, h in enumerate(sorted(row, reverse=True), 1)])
        return ans