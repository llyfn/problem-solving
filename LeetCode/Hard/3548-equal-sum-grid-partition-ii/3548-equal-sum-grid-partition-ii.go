func canPartitionGrid(grid [][]int) bool {
	total := 0
	for _, row := range grid {
		for _, val := range row {
			total += val
		}
	}
	for k := 0; k < 4; k++ {
		m, n := len(grid), len(grid[0])
		if m > 1 {
			sum, exist := 0, map[int]bool{0: true}
			if n == 1 {
				for i := 0; i < m-1; i++ {
					sum += grid[i][0]
					t := sum*2 - total
					if t == 0 || t == grid[0][0] || t == grid[i][0] { return true }
				}
			} else {
				for i := 0; i < m-1; i++ {
					for j := 0; j < n; j++ {
						exist[grid[i][j]] = true
						sum += grid[i][j]
					}
					t := sum*2 - total
					if i == 0 && (t == 0 || t == grid[0][0] || t == grid[0][n-1]) { return true }
					if i > 0 && exist[t] { return true }
				}
			}
		}
		rotated := make([][]int, n)
		for i := range rotated {
			rotated[i] = make([]int, m)
			for j := 0; j < m; j++ {
				rotated[i][m-1-j] = grid[j][i]
			}
		}
		grid = rotated
	}
	return false
}