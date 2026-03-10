const mod = 1_000_000_007

func numberOfStableArrays(zero, one, limit int) int {
	dp := make([][][2]int, zero+1)
	for i := range dp {
		dp[i] = make([][2]int, one+1)
		if i <= limit {
			dp[i][0][0] = 1
		}
	}
	for j := 0; j <= min(one, limit); j++ {
		dp[0][j][1] = 1
	}
	for i := 1; i <= zero; i++ {
		for j := 1; j <= one; j++ {
			v0, v1 := dp[i-1][j][0]+dp[i-1][j][1], dp[i][j-1][0]+dp[i][j-1][1]
			if i > limit {
				v0 -= dp[i-limit-1][j][1]
			}
			if j > limit {
				v1 -= dp[i][j-limit-1][0]
			}
			dp[i][j] = [2]int{(v0%mod + mod) % mod, (v1%mod + mod) % mod}
		}
	}
	return (dp[zero][one][0] + dp[zero][one][1]) % mod
}