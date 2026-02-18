class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[10**9] * len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0: dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == i: dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else: dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
        return min(dp[-1])