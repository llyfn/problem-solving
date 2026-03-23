func maxProductPath(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dpMax, dpMin := make([][]int64, m), make([][]int64, m)
	for i := range dpMax {
		dpMax[i], dpMin[i] = make([]int64, n), make([]int64, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			val := int64(grid[i][j])
			if i == 0 && j == 0 {
				dpMax[i][j], dpMin[i][j] = val, val
				continue
			}
			mx, mn := int64(-1e18), int64(1e18)
			if i > 0 {
				mx = max(mx, dpMax[i-1][j]*val, dpMin[i-1][j]*val)
				mn = min(mn, dpMax[i-1][j]*val, dpMin[i-1][j]*val)
			}
			if j > 0 {
				mx = max(mx, dpMax[i][j-1]*val, dpMin[i][j-1]*val)
				mn = min(mn, dpMax[i][j-1]*val, dpMin[i][j-1]*val)
			}
			dpMax[i][j], dpMin[i][j] = mx, mn
		}
	}
	return int(max(dpMax[m-1][n-1], -1) % 1_000_000_007)
}
