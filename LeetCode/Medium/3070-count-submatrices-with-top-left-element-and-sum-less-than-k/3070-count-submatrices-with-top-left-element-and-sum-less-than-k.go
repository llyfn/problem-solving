func countSubmatrices(grid [][]int, k int) (ans int) {
	for i := range grid {
		for j := range grid[i] {
			if i > 0 {
				grid[i][j] += grid[i-1][j]
			}
			if j > 0 {
				grid[i][j] += grid[i][j-1]
			}
			if i > 0 && j > 0 {
				grid[i][j] -= grid[i-1][j-1]
			}
			if grid[i][j] > k {
				break
			}
			ans++
		}
	}
	return
}
