class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        expanded = []
        for pos, limit in factory:
            for _ in range(limit):
                expanded.append(pos)
        
        n, m = len(robot), len(expanded)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for j in range(m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i][j-1]
                if dp[i-1][j-1] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + abs(robot[i-1] - expanded[j-1]))
        
        return dp[n][m]
