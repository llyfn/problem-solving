func canPartitionGrid(grid [][]int) bool {
	m, n := len(grid), len(grid[0])
	hSum, vSum, sum := make([]int, m), make([]int, n), 0
	for i, row := range grid {
		for j, v := range row {
			hSum[i], vSum[j], sum = hSum[i] + v, vSum[j] + v, sum + v
		}
	}
	for i, c := 0, 0; i < m - 1; i++ {
		c += hSum[i]
		if 2 * c == sum {
			return true
		}
	}
	for j, c := 0, 0; j < n - 1; j++ {
		c += vSum[j]
		if 2 * c == sum {
			return true
		}
	}
	return false
}