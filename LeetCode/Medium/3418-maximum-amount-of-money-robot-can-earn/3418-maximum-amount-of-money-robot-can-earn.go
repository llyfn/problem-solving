func maximumAmount(coins [][]int) int {
	m, n := len(coins), len(coins[0])
	dp := make([][][3]int, m)
	for i := range dp {
		dp[i] = make([][3]int, n)
		for j := range dp[i] {
			v := coins[i][j]
			for k := 0; k < 3; k++ {
				res := -int(1e9)
				if i == 0 && j == 0 {
					res = v
					if k > 0 {
						res = max(0, v)
					}
				}
				if i > 0 {
					res = max(res, dp[i-1][j][k]+v)
					if k > 0 {
						res = max(res, dp[i-1][j][k-1])
					}
				}
				if j > 0 {
					res = max(res, dp[i][j-1][k]+v)
					if k > 0 {
						res = max(res, dp[i][j-1][k-1])
					}
				}
				dp[i][j][k] = int(res)
			}
		}
	}
	return dp[m-1][n-1][2]
}